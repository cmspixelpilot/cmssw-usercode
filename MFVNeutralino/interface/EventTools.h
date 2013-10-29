#ifndef JMTucker_MFVNeutralino_interface_EventTools_h
#define JMTucker_MFVNeutralino_interface_EventTools_h

class TriggerHelper;

namespace mfv {
  static const int n_trigger_paths = 5;
  static const int n_clean_paths = 19+1;

  void trigger_decision(const TriggerHelper& trig, bool* pass_trigger);
}

#endif