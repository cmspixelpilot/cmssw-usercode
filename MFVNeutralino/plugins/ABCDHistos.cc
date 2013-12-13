#include "TH2F.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "JMTucker/MFVNeutralinoFormats/interface/VertexAux.h"

class ABCDHistos : public edm::EDAnalyzer {
 public:
  explicit ABCDHistos(const edm::ParameterSet&);
  void analyze(const edm::Event&, const edm::EventSetup&);

 private:
  const edm::InputTag vertex_src;

  TH1F* h_nsv;
  TH2F* h_ntracks01_maxtrackpt01;

};

ABCDHistos::ABCDHistos(const edm::ParameterSet& cfg)
  : vertex_src(cfg.getParameter<edm::InputTag>("vertex_src"))
{
  edm::Service<TFileService> fs;
  h_nsv = fs->make<TH1F>("h_nsv", ";number of secondary vertices;events", 15, 0, 15);
  h_ntracks01_maxtrackpt01 = fs->make<TH2F>("h_ntracks01_maxtrackpt01", ";sum of maxtrackpt for the two SV's with the highest ntracks;sum of ntracks for the two SV's with the highest ntracks", 300, 0, 300, 80, 0, 80);
}

void ABCDHistos::analyze(const edm::Event& event, const edm::EventSetup&) {

  edm::Handle<MFVVertexAuxCollection> vertices;
  event.getByLabel(vertex_src, vertices);

  const int nsv = int(vertices->size());
  h_nsv->Fill(nsv);

  if (nsv >= 2) {
    const MFVVertexAux& v0 = vertices->at(0);
    const MFVVertexAux& v1 = vertices->at(1);
    h_ntracks01_maxtrackpt01->Fill(v0.maxtrackpt + v1.maxtrackpt, v0.ntracks + v1.ntracks);
  }

}

DEFINE_FWK_MODULE(ABCDHistos);
