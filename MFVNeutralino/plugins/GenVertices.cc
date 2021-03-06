#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "JMTucker/Tools/interface/GenUtilities.h"
#include "JMTucker/MFVNeutralino/interface/MCInteractionMFV3j.h"
#include "JMTucker/Tools/interface/MCInteractionTops.h"

class MFVGenVertices : public edm::EDProducer {
public:
  explicit MFVGenVertices(const edm::ParameterSet&);

private:
  virtual void produce(edm::Event&, const edm::EventSetup&);

  const edm::InputTag gen_src;
  const edm::InputTag beamspot_src;
  const bool debug;
};

MFVGenVertices::MFVGenVertices(const edm::ParameterSet& cfg) 
  : gen_src(cfg.getParameter<edm::InputTag>("gen_src")),
    beamspot_src(cfg.getParameter<edm::InputTag>("beamspot_src")),
    debug(cfg.getUntrackedParameter<bool>("debug", false))
{
  produces<std::vector<double> >();
}

void MFVGenVertices::produce(edm::Event& event, const edm::EventSetup&) {
  edm::Handle<reco::GenParticleCollection> gen_particles;
  event.getByLabel(gen_src, gen_particles);

  edm::Handle<reco::BeamSpot> beamspot;
  event.getByLabel(beamspot_src, beamspot);

  std::auto_ptr<std::vector<double> > decay_vertices(new std::vector<double>);

  bool ok = false;

  if (!event.isRealData()) {
    MCInteractionMFV3j mci;
    mci.Init(*gen_particles);
    if (mci.Valid()) {
      for (int i = 0; i < 2; ++i) {
        const reco::GenParticle* daughter = mci.stranges[i];
        decay_vertices->push_back(daughter->vx());
        decay_vertices->push_back(daughter->vy());
        decay_vertices->push_back(daughter->vz());
      }
      ok = true;
      if (debug) printf("mci valid: ");
    }
  }

  if (!ok) {
    for (int i = 0; i < 2; ++i) {
      decay_vertices->push_back(beamspot->x0());
      decay_vertices->push_back(beamspot->y0());
      decay_vertices->push_back(beamspot->z0());
    }
    if (debug) printf("mci INVALID: ");
  }

  if (debug) {
    for (double d : *decay_vertices)
      printf("%6.3f ", d);
    printf("\n");
  }

  event.put(decay_vertices);
}

DEFINE_FWK_MODULE(MFVGenVertices);
