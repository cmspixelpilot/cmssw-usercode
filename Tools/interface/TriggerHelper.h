#ifndef JMTucker_Tools_TriggerHelper_h
#define JMTucker_Tools_TriggerHelper_h

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/Event.h"

struct TriggerHelper {
  const edm::TriggerResults& trigger_results;
  const edm::TriggerNames& trigger_names;

  bool debug;

  static const edm::TriggerResults& _get(const edm::Event& event, const edm::InputTag& src) {
    edm::Handle<edm::TriggerResults> h;
    event.getByLabel(src, h);
    return *h;
  }

  TriggerHelper(const edm::TriggerResults& trigger_results_, const edm::TriggerNames& trigger_names_) : trigger_results(trigger_results_), trigger_names(trigger_names_), debug(false) {}
  TriggerHelper(const edm::Event& event, const edm::InputTag& src)
    : trigger_results(_get(event, src)), trigger_names(event.triggerNames(trigger_results)), debug(false) {}

  bool pass(const std::string& name, bool& found) const {
    const unsigned ndx = trigger_names.triggerIndex(name);
    found = ndx < trigger_results.size();
    if (debug) {
      printf("TriggerHelper debug\nname: %s\n", name.c_str());
      printf("names size: %lu\n", trigger_names.size());
      for (size_t i = 0, ie= trigger_names.size(); i < ie; ++i)
	printf("name %lu: %s\n", i, trigger_names.triggerName(i).c_str());
      printf("ndx: %u => name %s found? %i\n", ndx, name.c_str(), found);
      if (found)
	printf("trigger fired? %i\n", trigger_results.accept(ndx));
      printf("done.\n");
    }
    return found ? trigger_results.accept(ndx) : false;
  }

  bool pass(const std::string& name) const {
    bool found = false;
    bool result = pass(name, found);
    if (!found)
      throw cms::Exception("TriggerHelper") << "no trigger with name " << name << " found\n";
    return result;
  }
   
  bool pass(const char* fmt, int range_lo, int range_hi, bool throw_not_found=true) const {
    char name[512];
    for (int i = range_lo; i <= range_hi; ++i) {
      snprintf(name, 512, fmt, i);
      bool found = false;
      bool result = pass(name, found);
      if (found)
	return result;
    }
    if (throw_not_found)
      throw cms::Exception("TriggerHelper") << "no trigger for fmt " << fmt << " range " << range_lo << "-" << range_hi << " found";
    return false;
  }

  bool pass_any_version(const std::string& trigger, bool throw_not_found=true) const {
    for (size_t ipath = 0, ipathe = trigger_names.size(); ipath < ipathe; ++ipath) {
      const std::string path = trigger_names.triggerName(ipath);
      if (path.substr(0, trigger.size()) == trigger)
        return trigger_results.accept(ipath);
    }
    
    if (throw_not_found)
      throw cms::Exception("TriggerHelper") << "no trigger for " << trigger << " found";
    return false;
  }
};

#endif
