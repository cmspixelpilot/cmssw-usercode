#include "TH2F.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

class MFVJetVertexAssociator : public edm::EDProducer {
public:
  MFVJetVertexAssociator(const edm::ParameterSet&);

  virtual void produce(edm::Event&, const edm::EventSetup&);

private:
  typedef edm::Association<reco::VertexCollection> JetVertexAssociation;

  const edm::InputTag jet_src;
  const edm::InputTag vertex_src;
  const double min_jet_track_frac;
  const double min_vertex_track_weight;
  const bool verbose;
  const bool histos;

  TH2F* h_n_jets_v_vertices;
  TH1F* h_n_jet_tracks;
  TH1F* h_frac;
  TH2F* h_n_fracs;
};

MFVJetVertexAssociator::MFVJetVertexAssociator(const edm::ParameterSet& cfg)
  : jet_src(cfg.getParameter<edm::InputTag>("jet_src")),
    vertex_src(cfg.getParameter<edm::InputTag>("vertex_src")),
    min_jet_track_frac(cfg.getParameter<double>("min_jet_track_frac")),
    min_vertex_track_weight(cfg.getParameter<double>("min_vertex_track_weight")),
    verbose(cfg.getUntrackedParameter<bool>("verbose", false)),
    histos(cfg.getUntrackedParameter<bool>("histos", false))
{
  produces<JetVertexAssociation>();

  if (histos) {
    edm::Service<TFileService> fs;
    
    h_n_jets_v_vertices = fs->make<TH2F>("h_n_jets_v_vertices", ";# of vertices;# of jets", 30, 0, 30, 30, 0, 30);
    h_n_jet_tracks = fs->make<TH1F>("h_n_jet_tracks", ";# tracks per jet;arb. units", 50, 0, 50);
    h_frac = fs->make<TH1F>("h_frac", ";fraction of jet's tracks in a vertex;arb. units", 51, 0, 1.02);
    h_n_fracs = fs->make<TH2F>("h_n_fracs", ";# non zero fractions;# non zero good fractions", 30, 0, 30, 30, 0, 30);
  }
}

void MFVJetVertexAssociator::produce(edm::Event& event, const edm::EventSetup&) {
  edm::Handle<pat::JetCollection> jets;
  event.getByLabel(jet_src, jets);

  edm::Handle<reco::VertexCollection> vertices;
  event.getByLabel(vertex_src, vertices);

  std::auto_ptr<JetVertexAssociation> assoc(new JetVertexAssociation);
  JetVertexAssociation::Filler filler(*assoc);
  
  const size_t n_jets = jets->size();
  const size_t n_vertices = vertices->size();

  if (histos)
    h_n_jets_v_vertices->Fill(n_vertices, n_jets);

  std::vector<int> indices(n_jets);
  for (size_t ijet = 0; ijet < n_jets; ++ijet) {
    int assoc_ivtx = -1;
    const pat::Jet& jet = jets->at(ijet);
    std::set<reco::TrackRef> jet_tracks;
    for (const reco::PFCandidatePtr& pfcand : jet.getPFConstituents()) {
      const reco::TrackRef& tk = pfcand->trackRef();
      if (tk.isNonnull())
        jet_tracks.insert(tk);
    }

    const size_t n_jet_tracks = jet_tracks.size();
    if (histos)
      h_n_jet_tracks->Fill(n_jet_tracks);

    if (n_jet_tracks > 0) {
      double best_frac = 0;
      int n_non_zero_fracs = 0;
      int n_non_zero_good_fracs = 0;

      for (size_t ivtx = 0; ivtx < n_vertices; ++ivtx) {
        const reco::Vertex& vtx = vertices->at(ivtx);

        int in_jet = 0;
        for (auto itk = vtx.tracks_begin(), itke = vtx.tracks_end(); itk != itke; ++itk) {
          if (vtx.trackWeight(*itk) > min_vertex_track_weight) {
            reco::TrackRef tk = itk->castTo<reco::TrackRef>();
            if (jet_tracks.count(tk) > 0)
              ++in_jet;
          }
        }
      
        double frac = double(in_jet)/n_jet_tracks;
        if (histos) {
          if (in_jet > 0)
            ++n_non_zero_fracs;
          h_frac->Fill(frac);
        }

        if (frac > min_jet_track_frac) {
          if (histos)
            ++n_non_zero_good_fracs;

          if (frac > best_frac) {
            best_frac = frac;
            assoc_ivtx = ivtx;
          }
        }
      }

      if (histos)
        h_n_fracs->Fill(n_non_zero_fracs, n_non_zero_good_fracs);
    }

    indices[ijet] = assoc_ivtx;
  }

  filler.insert(jets, indices.begin(), indices.end());
  filler.fill();
  event.put(assoc);
}

DEFINE_FWK_MODULE(MFVJetVertexAssociator);