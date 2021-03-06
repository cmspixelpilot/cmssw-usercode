#include "TTree.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "JMTucker/MFVNeutralino/interface/MovedTracksNtuple.h"
#include "JMTucker/MFVNeutralinoFormats/interface/Event.h"
#include "JMTucker/MFVNeutralinoFormats/interface/VertexAux.h"

class MFVMovedTracksTreer : public edm::EDAnalyzer {
public:
  explicit MFVMovedTracksTreer(const edm::ParameterSet&);
  void analyze(const edm::Event&, const edm::EventSetup&);

  const edm::InputTag event_src;
  const edm::InputTag vertices_src;
  const edm::InputTag weight_src;
  const std::string mover_src;
  const double max_dist2move;
  const bool apply_presel;
  const unsigned njets_req;
  const unsigned nbjets_req;

  mfv::MovedTracksNtuple nt;
  TTree* tree;
};

MFVMovedTracksTreer::MFVMovedTracksTreer(const edm::ParameterSet& cfg)
  : event_src(cfg.getParameter<edm::InputTag>("event_src")),
    vertices_src(cfg.getParameter<edm::InputTag>("vertices_src")),
    weight_src(cfg.getParameter<edm::InputTag>("weight_src")),
    mover_src(cfg.getParameter<std::string>("mover_src")),
    max_dist2move(cfg.getParameter<double>("max_dist2move")),
    apply_presel(cfg.getParameter<bool>("apply_presel")),
    njets_req(cfg.getParameter<unsigned>("njets_req")),
    nbjets_req(cfg.getParameter<unsigned>("nbjets_req"))
{
  edm::Service<TFileService> fs;

  tree = fs->make<TTree>("t", "");
  nt.write_to_tree(tree);
}

void MFVMovedTracksTreer::analyze(const edm::Event& event, const edm::EventSetup&) {
  nt.clear();

  nt.run   = event.id().run();
  nt.lumi  = event.luminosityBlock();
  nt.event = event.id().event();

  edm::Handle<double> weight;
  event.getByLabel(weight_src, weight);
  nt.weight = *weight;

  edm::Handle<MFVEvent> mevent;
  event.getByLabel(event_src, mevent);

  nt.npu = int(mevent->npu);
  nt.npv = mevent->npv;
  nt.pvx = mevent->pvx - mevent->bsx_at_z(mevent->pvz);
  nt.pvy = mevent->pvy - mevent->bsy_at_z(mevent->pvz);
  nt.pvz = mevent->pvz;
  nt.pvntracks = mevent->pv_ntracks;
  nt.pvsumpt2 = mevent->pv_sumpt2;
  nt.jetsumht = mevent->jet_sum_ht();
  nt.jetpt4 = mevent->jetpt4();
  nt.met = mevent->met();
  nt.nlep = mevent->nlep(2);
  nt.nalljets = mevent->njets();

  edm::Handle<reco::TrackCollection> tracks, moved_tracks;
  edm::Handle<int> npreseljets, npreselbjets;
  edm::Handle<pat::JetCollection> jets_used, bjets_used;
  edm::Handle<std::vector<double> > move_vertex;
  event.getByLabel(edm::InputTag(mover_src),                 tracks);
  event.getByLabel(edm::InputTag(mover_src, "moved"),        moved_tracks);
  event.getByLabel(edm::InputTag(mover_src, "npreseljets"),  npreseljets); 
  event.getByLabel(edm::InputTag(mover_src, "npreselbjets"), npreselbjets); 
  event.getByLabel(edm::InputTag(mover_src, "jetsUsed"),     jets_used);
  event.getByLabel(edm::InputTag(mover_src, "bjetsUsed"),    bjets_used);
  event.getByLabel(edm::InputTag(mover_src, "moveVertex"),   move_vertex);

  nt.ntracks = tracks->size();
  nt.nseltracks = moved_tracks->size();

  nt.npreseljets  = *npreseljets;
  nt.npreselbjets = *npreselbjets;

  nt.nlightjets = jets_used->size();

  for (const pat::JetCollection* jets : { &*jets_used, &*bjets_used }) {
    for (const pat::Jet& jet : *jets) {
      nt.jets_pt.push_back(jet.pt());
      nt.jets_eta.push_back(jet.eta());
      nt.jets_phi.push_back(jet.phi());
      nt.jets_energy.push_back(jet.energy());

      ushort jet_ntracks = 0;
      for (const reco::PFCandidatePtr& pfcand : jet.getPFConstituents())
        if (pfcand->trackRef().isNonnull())
          ++jet_ntracks;
      nt.jets_ntracks.push_back(jet_ntracks);
    }
  }

  nt.move_z = move_vertex->at(2);
  nt.move_x = move_vertex->at(0) - mevent->bsx_at_z(nt.move_z);
  nt.move_y = move_vertex->at(1) - mevent->bsy_at_z(nt.move_z);

  edm::Handle<MFVVertexAuxCollection> vertices;
  event.getByLabel(vertices_src, vertices);

  for (const MFVVertexAux& v : *vertices) {
    const double vx = v.x - mevent->bsx_at_z(v.z);
    const double vy = v.y - mevent->bsy_at_z(v.z);
    const double vz = v.z;

    const double dist2move = pow(pow(vx - nt.move_x, 2) +
                                 pow(vy - nt.move_y, 2) +
                                 pow(vz - nt.move_z, 2), 0.5);
    if (dist2move > max_dist2move)
      continue;

    nt.vtxs_x.push_back(vx);
    nt.vtxs_y.push_back(vy);
    nt.vtxs_z.push_back(vz);
    nt.vtxs_theta.push_back(2*atan(exp(-v.eta[mfv::PTracksPlusJetsByNtracks])));
    nt.vtxs_phi.push_back(v.phi[mfv::PTracksPlusJetsByNtracks]);
    nt.vtxs_ntracks.push_back(v.ntracks());
    nt.vtxs_ntracksptgt3.push_back(v.ntracksptgt(3));
    nt.vtxs_drmin.push_back(v.drmin());
    nt.vtxs_drmax.push_back(v.drmax());
    nt.vtxs_bs2derr.push_back(v.bs2derr);
  }

  if (apply_presel &&
      (nt.npreseljets < njets_req ||
       nt.npreselbjets < nbjets_req ||
       nt.jetsumht < 500 ||
       nt.jetpt4 < 60)
      )
    return;

  tree->Fill();
}

DEFINE_FWK_MODULE(MFVMovedTracksTreer);
