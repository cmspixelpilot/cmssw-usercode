#include "TH2F.h"
#include "TRandom3.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "JMTucker/Tools/interface/TriggerHelper.h"
#include "JMTucker/Tools/interface/Utilities.h"
#include "JMTucker/MFVNeutralinoFormats/interface/Event.h"
#include "JMTucker/MFVNeutralino/interface/EventTools.h"

#define NBDISC 2

class MFVEventHistos : public edm::EDAnalyzer {
 public:
  explicit MFVEventHistos(const edm::ParameterSet&);
  void analyze(const edm::Event&, const edm::EventSetup&);

 private:
  const edm::InputTag mfv_event_src;
  const std::vector<double> force_bs;
  const edm::InputTag primary_vertex_src;
  const edm::InputTag jets_src;
  const edm::InputTag weight_src;
  const bool re_trigger;

  TH1F* h_w;

  TH2F* h_gen_decay;
  TH1F* h_gen_partons_in_acc;

  TH1F* h_minlspdist2d;
  TH1F* h_lspdist2d;
  TH1F* h_lspdist3d;

  TH1F* h_pass_trigger[mfv::n_trigger_paths];
  TH1F* h_pass_clean[mfv::n_clean_paths];
  TH1F* h_pass_clean_all;
  TH1F* h_passoldskim;

  TH1F* h_npfjets;
  TH1F* h_pfjetpt4;
  TH1F* h_pfjetpt5;
  TH1F* h_pfjetpt6;

  TH1F* h_npu;

  TH1F* h_bsx;
  TH1F* h_bsy;
  TH1F* h_bsz;
  TH1F* h_bsphi;

  TH1F* h_npv;
  TH1F* h_pvx;
  TH1F* h_pvy;
  TH1F* h_pvz;
  TH1F* h_pvrho;
  TH1F* h_pvphi;
  TH1F* h_pvntracks;
  TH1F* h_pvsumpt2;

  TH1F* h_njets;
  TH1F* h_njetsnopu[3];
  TH1F* h_jetpt4;
  TH1F* h_jetpt5;
  TH1F* h_jetpt6;
  TH1F* h_jet_sum_ht;
  TH1F* h_jetphi;
  TH1F* h_jetpairdphi;

  TH1F* h_sv0phi;
  TH1F* h_sv1phi;
  TH1F* h_sv0jetdphi;
  TH1F* h_sv1jetdphi;
  TH1F* h_svpairdphi;
  TH1F* h_svpairdphi_cut;

  //TH1F* h_bs2ddist1v;
  TH1F* h_sv0bs2ddist;
  TH1F* h_sv1bs2ddist;
  TH1F* h_svpairdist;
  TH1F* h_svpairdist_cut;
  TH2F* h_svdist_dphi;
  TH2F* h_svdist_bs2ddist0;
  TH2F* h_svdist_bs2ddist1;
  TH2F* h_bs2ddist1_bs2ddist0;

  TH1F* h_metx;
  TH1F* h_mety;
  TH1F* h_metsig;
  TH1F* h_met;
  TH1F* h_metphi;
  TH1F* h_metdphimin;

  TH1F* h_nbtags[3];
  TH1F* h_nmuons[3];
  TH1F* h_nelectrons[3];
  TH1F* h_nleptons[3];

  TH1F* h_bjets_absdphi[3][2];
  TH1F* h_bjets_dphi[3][2];
  TH1F* h_bjets_deta[3][2];
  TH2F* h_bjets_deta_dphi[3][2];
  TH1F* h_bjets_avgeta[3][2];
  TH2F* h_bjets_avgeta_dphi[3][2];
  TH1F* h_bjets_dR[3][2];
  TH2F* h_bjets_dR_dphi[3][2];

  TH1F* h_muons_absdphi[3];
  TH1F* h_muons_dphi[3];
  TH1F* h_muons_deta[3];
  TH2F* h_muons_deta_dphi[3];
  TH1F* h_muons_avgeta[3];
  TH2F* h_muons_avgeta_dphi[3];
  TH1F* h_muons_dR[3];
  TH2F* h_muons_dR_dphi[3];

  TH1F* h_pv_n;
  TH1F* h_pv_x[4];
  TH1F* h_pv_y[4];
  TH1F* h_pv_z[4];
  TH1F* h_pv_rho[4];
  TH1F* h_pv_phi[4];
  TH1F* h_pv_ntracks[4];
  TH1F* h_pv_sumpt2[4];

  TH1F* h_jets_n;
  TH1F* h_jets_pt;
  TH1F* h_jets_eta;
  TH1F* h_jets_phi;

  TH1F* h_bjets_n[NBDISC][3];
  TH1F* h_bjets_pt[NBDISC][3];
  TH1F* h_bjets_eta[NBDISC][3];
  TH1F* h_bjets_phi[NBDISC][3];
};

MFVEventHistos::MFVEventHistos(const edm::ParameterSet& cfg)
  : mfv_event_src(cfg.getParameter<edm::InputTag>("mfv_event_src")),
    force_bs(cfg.getParameter<std::vector<double> >("force_bs")),
    primary_vertex_src(cfg.getParameter<edm::InputTag>("primary_vertex_src")),
    jets_src(cfg.getParameter<edm::InputTag>("jets_src")),
    weight_src(cfg.getParameter<edm::InputTag>("weight_src")),
    re_trigger(cfg.getParameter<bool>("re_trigger"))
{
  if (force_bs.size() && force_bs.size() != 3)
    throw cms::Exception("Misconfiguration", "force_bs must be empty or size 3");

  edm::Service<TFileService> fs;
  gRandom->SetSeed(0);
  //TFile* f = TFile::Open("aaaa.root");
  //h_bs2ddist1v = (TH1F*)(f->Get("bs2ddist1v"))->Clone();
  //f->Close();
  //delete f;

  h_w = fs->make<TH1F>("h_w", ";event weight;events/0.1", 100, 0, 10);

  h_gen_decay = fs->make<TH2F>("h_gen_decay", "0-2=e,mu,tau, 3=h;decay code #0;decay code #1", 4, 0, 4, 4, 0, 4);
  h_gen_partons_in_acc = fs->make<TH1F>("h_gen_partons_in_acc", ";# partons from LSP in acceptance;events", 11, 0, 11);

  h_minlspdist2d = fs->make<TH1F>("h_minlspdist2d", ";min dist2d(gen vtx #i) (cm);events/0.1 mm", 200, 0, 2);
  h_lspdist2d = fs->make<TH1F>("h_lspdist2d", ";dist2d(gen vtx #0, #1) (cm);events/0.1 mm", 200, 0, 2);
  h_lspdist3d = fs->make<TH1F>("h_lspdist3d", ";dist3d(gen vtx #0, #1) (cm);events/0.1 mm", 200, 0, 2);

  for (int i = 0; i < mfv::n_trigger_paths; ++i)
    h_pass_trigger[i] = fs->make<TH1F>(TString::Format("h_pass_trigger_%i", i), TString::Format(";pass_trigger[%i];events", i), 2, 0, 2);
  for (int i = 0; i < mfv::n_clean_paths; ++i)
    h_pass_clean[i] = fs->make<TH1F>(TString::Format("h_pass_clean_%i", i), TString::Format(";pass_clean[%i];events", i), 2, 0, 2);
  h_pass_clean_all = fs->make<TH1F>("h_pass_clean_all", ";pass_clean_all;events", 2, 0, 2);
  h_passoldskim = fs->make<TH1F>("h_passoldskim", ";pass old skim?;events", 2, 0, 2);

  h_npfjets = fs->make<TH1F>("h_npfjets", ";# of PF jets;events", 30, 0, 30);
  h_pfjetpt4 = fs->make<TH1F>("h_pfjetpt4", ";p_{T} of 4th PF jet (GeV);events/5 GeV", 100, 0, 500);
  h_pfjetpt5 = fs->make<TH1F>("h_pfjetpt5", ";p_{T} of 5th PF jet (GeV);events/5 GeV", 100, 0, 500);
  h_pfjetpt6 = fs->make<TH1F>("h_pfjetpt6", ";p_{T} of 6th PF jet (GeV);events/5 GeV", 100, 0, 500);

  h_npu = fs->make<TH1F>("h_npu", ";true nPU;events", 65, 0, 65);

  h_bsx = fs->make<TH1F>("h_bsx", ";beamspot x (cm);events/0.1 mm", 200, -1, 1);
  h_bsy = fs->make<TH1F>("h_bsy", ";beamspot y (cm);events/0.1 mm", 200, -1, 1);
  h_bsz = fs->make<TH1F>("h_bsz", ";beamspot z (cm);events/mm", 200, -10, 10);
  h_bsphi = fs->make<TH1F>("h_bsphi", ";beamspot #phi (rad);events/.063", 100, -3.1416, 3.1416);

  h_npv = fs->make<TH1F>("h_npv", ";# of primary vertices;events", 65, 0, 65);
  h_pvx = fs->make<TH1F>("h_pvx", ";primary vertex x (cm);events/10 #mum", 200, -0.1, 0.1);
  h_pvy = fs->make<TH1F>("h_pvy", ";primary vertex y (cm);events/10 #mum", 200, -0.1, 0.1);
  h_pvz = fs->make<TH1F>("h_pvz", ";primary vertex z (cm);events/1.5 mm", 200, -15, 15);
  h_pvrho = fs->make<TH1F>("h_pv_rho", ";PV rho (cm);events/5 #mum", 200, 0, 0.1);
  h_pvphi = fs->make<TH1F>("h_pv_phi", ";primary vertex #phi (rad);events/.063", 100, -3.1416, 3.1416);
  h_pvntracks = fs->make<TH1F>("h_pv_ntracks", ";# of tracks in primary vertex;events", 200, 0, 200);
  h_pvsumpt2 = fs->make<TH1F>("h_pv_sumpt2", ";PV #Sigma p_{T}^{2} (GeV^{2});events/100 GeV^{2}", 200, 0, 20000);

  const char* lmt_ex[3] = {"loose", "medium", "tight"};

  h_njets = fs->make<TH1F>("h_njets", ";# of jets;events", 20, 0, 20);
  for (int i = 0; i < 3; ++i)
    h_njetsnopu[i] = fs->make<TH1F>(TString::Format("h_njetsnopu_%s", lmt_ex[i]), TString::Format(";# of jets (%s PU id);events", lmt_ex[i]), 20, 0, 20);
  h_jetpt4 = fs->make<TH1F>("h_jetpt4", ";p_{T} of 4th jet (GeV);events/5 GeV", 100, 0, 500);
  h_jetpt5 = fs->make<TH1F>("h_jetpt5", ";p_{T} of 5th jet (GeV);events/5 GeV", 100, 0, 500);
  h_jetpt6 = fs->make<TH1F>("h_jetpt6", ";p_{T} of 6th jet (GeV);events/5 GeV", 100, 0, 500);
  h_jet_sum_ht = fs->make<TH1F>("h_jet_sum_ht", ";#Sigma H_{T} of jets (GeV);events/25 GeV", 200, 0, 5000);
  h_jetphi = fs->make<TH1F>("h_jetphi", ";jets #phi (rad);jets/.063", 100, -3.1416, 3.1416);
  h_jetpairdphi = fs->make<TH1F>("h_jetpairdphi", ";jet pair #Delta#phi (rad);jet pairs/.063", 100, -3.1416, 3.1416);

  h_sv0phi = fs->make<TH1F>("h_sv0phi", ";constructed SV0 #phi (rad);events/.126", 50, -3.15, 3.15);
  h_sv1phi = fs->make<TH1F>("h_sv1phi", ";constructed SV1 #phi (rad);events/.126", 50, -3.15, 3.15);
  h_sv0jetdphi = fs->make<TH1F>("h_sv0jetdphi", ";constructed #Delta#phi(SV0, jets) (rad);jets/.126", 50, -3.15, 3.15);
  h_sv1jetdphi = fs->make<TH1F>("h_sv1jetdphi", ";constructed #Delta#phi(SV1, jets) (rad);jets/.126", 50, -3.15, 3.15);
  h_svpairdphi = fs->make<TH1F>("h_svpairdphi", ";constructed vertex pair #Delta#phi (rad);events/.126", 50, -3.15, 3.15);
  h_svpairdphi_cut = fs->make<TH1F>("h_svpairdphi_cut", "#Delta#phi with space clearing;constructed vertex pair #Delta#phi (rad);events/.126", 50, -3.15, 3.15);

  h_sv0bs2ddist = fs->make<TH1F>("h_sv0bs2ddist", ";constructed SV0 distance (cm);vertices", 500, 0, 1);
  h_sv1bs2ddist = fs->make<TH1F>("h_sv1bs2ddist", ";constructed SV1 distance (cm);vertices", 500, 0, 1);
  h_svpairdist = fs->make<TH1F>("h_svpairdist", ";constructed vertex pair distance (cm);events", 200, 0, 0.2);
  h_svpairdist_cut = fs->make<TH1F>("h_svpairdist_cut", "svdist2d with space clearing;constructed vertex pair distance (cm);events", 200, 0, 0.2);
  h_svdist_dphi = fs->make<TH2F>("h_svdist_dphi", "constructed vertex pair;#Delta#phi (rad);distance (cm)", 50, -3.15, 3.15, 200, 0, 0.2);
  h_svdist_bs2ddist0 = fs->make<TH2F>("h_svdist_bs2ddist0", ";bs2ddist0;svdist2d", 500, 0, 1, 1000, 0, 2);
  h_svdist_bs2ddist1 = fs->make<TH2F>("h_svdist_bs2ddist1", ";bs2ddist1;svdist2d", 500, 0, 1, 1000, 0, 2);
  h_bs2ddist1_bs2ddist0 = fs->make<TH2F>("h_bs2ddist1_bs2ddist0", ";bs2ddist0;bs2ddist1", 500, 0, 1, 500, 0, 1);

  h_metx = fs->make<TH1F>("h_metx", ";MET x (GeV);events/5 GeV", 100, -250, 250);
  h_mety = fs->make<TH1F>("h_mety", ";MET y (GeV);events/5 GeV", 100, -250, 250);
  h_metsig = fs->make<TH1F>("h_metsig", ";MET significance;events/0.5", 100, 0, 50);
  h_met = fs->make<TH1F>("h_met", ";MET (GeV);events/5 GeV", 100, 0, 500);
  h_metphi = fs->make<TH1F>("h_metphi", ";MET #phi (rad);events/.063", 100, -3.1416, 3.1416);
  h_metdphimin = fs->make<TH1F>("h_metdphimin", ";#Delta #hat{#phi}_{min} (rad);events/0.1", 100, 0, 10);

  const char* lep_ex[3] = {"veto", "semilep", "dilep"};
  const char* bjets_pt[2] = {"20", "50"};
  for (int i = 0; i < 3; ++i) {
    h_nbtags[i] = fs->make<TH1F>(TString::Format("h_nbtags_%s", lmt_ex[i]), TString::Format(";# of %s b-tags;events", lmt_ex[i]), 20, 0, 20);
    h_nmuons[i] = fs->make<TH1F>(TString::Format("h_nmuons_%s", lep_ex[i]), TString::Format(";# of %s muons;events", lep_ex[i]), 5, 0, 5);
    h_nelectrons[i] = fs->make<TH1F>(TString::Format("h_nelectrons_%s", lep_ex[i]), TString::Format(";# of %s electrons;events", lep_ex[i]), 5, 0, 5);
    h_nleptons[i] = fs->make<TH1F>(TString::Format("h_nleptons_%s", lep_ex[i]), TString::Format(";# of %s leptons;events", lep_ex[i]), 5, 0, 5);

    for (int j = 0; j < 2; ++j) {
      h_bjets_absdphi[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s_ptgt%s_absdphi", lmt_ex[i], bjets_pt[j]), TString::Format("events with two %s GeV %s bjets;|#Delta#phi| (rad);events/0.126", bjets_pt[j], lmt_ex[i]), 25, 0, 3.15);
      h_bjets_dphi[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s_ptgt%s_dphi", lmt_ex[i], bjets_pt[j]), TString::Format("events with two %s GeV %s bjets;#Delta#phi (rad);events/0.126", bjets_pt[j], lmt_ex[i]), 50, -3.15, 3.15);
      h_bjets_deta[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s_ptgt%s_deta", lmt_ex[i], bjets_pt[j]), TString::Format("events with two %s GeV %s bjets;#Delta#eta (rad);events/0.16", bjets_pt[j], lmt_ex[i]), 50, -4, 4);
      h_bjets_deta_dphi[i][j] = fs->make<TH2F>(TString::Format("h_bjets_%s_ptgt%s_deta_dphi", lmt_ex[i], bjets_pt[j]), TString::Format("events with two %s GeV %s bjets;#Delta#phi (rad);#Delta#eta (rad)", bjets_pt[j], lmt_ex[i]), 50, -3.15, 3.15, 50, -4, 4);
      h_bjets_avgeta[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s_ptgt%s_avgeta", lmt_ex[i], bjets_pt[j]), TString::Format("events with two %s GeV %s bjets;avg #eta (rad);events/0.16", bjets_pt[j], lmt_ex[i]), 50, -4, 4);
      h_bjets_avgeta_dphi[i][j] = fs->make<TH2F>(TString::Format("h_bjets_%s_ptgt%s_avgeta_dphi", lmt_ex[i], bjets_pt[j]), TString::Format("events with two %s GeV %s bjets;#Delta#phi (rad); avg #eta (rad)", bjets_pt[j], lmt_ex[i]), 50, -3.15, 3.15, 50, -4, 4);
      h_bjets_dR[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s_ptgt%s_dR", lmt_ex[i], bjets_pt[j]), TString::Format("events with two %s GeV %s bjets;#Delta R (rad); events/0.14", bjets_pt[j], lmt_ex[i]), 50, 0, 7);
      h_bjets_dR_dphi[i][j] = fs->make<TH2F>(TString::Format("h_bjets_%s_ptgt%s_dR_dphi", lmt_ex[i], bjets_pt[j]), TString::Format("events with two %s GeV %s bjets;#Delta#phi (rad);#Delta R (rad)", bjets_pt[j], lmt_ex[i]), 50, -3.15, 3.15, 50, 0, 7);
    }

    h_muons_absdphi[i] = fs->make<TH1F>(TString::Format("h_muons_%s_absdphi", lep_ex[i]), TString::Format("events with two %s muons;|#Delta#phi| (rad);events/0.126", lep_ex[i]), 25, 0, 3.15);
    h_muons_dphi[i] = fs->make<TH1F>(TString::Format("h_muons_%s_dphi", lep_ex[i]), TString::Format("events with two %s muons;#Delta#phi (rad);events/0.126", lep_ex[i]), 50, -3.15, 3.15);
    h_muons_deta[i] = fs->make<TH1F>(TString::Format("h_muons_%s_deta", lep_ex[i]), TString::Format("events with two %s muons;#Delta#eta (rad);events/0.16", lep_ex[i]), 50, -4, 4);
    h_muons_deta_dphi[i] = fs->make<TH2F>(TString::Format("h_muons_%s_deta_dphi", lep_ex[i]), TString::Format("events with two %s muons;#Delta#phi (rad);#Delta#eta (rad)", lep_ex[i]), 50, -3.15, 3.15, 50, -4, 4);
    h_muons_avgeta[i] = fs->make<TH1F>(TString::Format("h_muons_%s_avgeta", lep_ex[i]), TString::Format("events with two %s muons;avg #eta (rad);events/0.16", lep_ex[i]), 50, -4, 4);
    h_muons_avgeta_dphi[i] = fs->make<TH2F>(TString::Format("h_muons_%s_avgeta_dphi", lep_ex[i]), TString::Format("events with two %s muons;#Delta#phi (rad);avg #eta (rad)", lep_ex[i]), 50, -3.15, 3.15, 50, -4, 4);
    h_muons_dR[i] = fs->make<TH1F>(TString::Format("h_muons_%s_dR", lep_ex[i]), TString::Format("events with two %s muons;#Delta R (rad);events/0.14", lep_ex[i]), 50, 0, 7);
    h_muons_dR_dphi[i] = fs->make<TH2F>(TString::Format("h_muons_%s_dR_dphi", lep_ex[i]), TString::Format("events with two %s muons;#Delta#phi (rad);#Delta R (rad)", lep_ex[i]), 50, -3.15, 3.15, 50, 0, 7);
  }

  if (primary_vertex_src.label() != "") {
    h_pv_n = fs->make<TH1F>("h_pv_n", ";# of primary vertices;events", 65, 0, 65);
    const char* pv_names[4] = {"pv1_sumpt2", "rest_sumpt2", "pv1_absdz", "rest_absdz"};
    for (int i = 0; i < 4; ++i) {
      h_pv_x[i] = fs->make<TH1F>(TString::Format("h_%s_x", pv_names[i]), TString::Format(";%s x (cm);events/10 #mum", pv_names[i]), 200, -0.1, 0.1);
      h_pv_y[i] = fs->make<TH1F>(TString::Format("h_%s_y", pv_names[i]), TString::Format(";%s y (cm);events/10 #mum", pv_names[i]), 200, -0.1, 0.1);
      h_pv_z[i] = fs->make<TH1F>(TString::Format("h_%s_z", pv_names[i]), TString::Format(";%s z (cm);events/1.5 mm", pv_names[i]), 200, -15, 15);
      h_pv_rho[i] = fs->make<TH1F>(TString::Format("h_%s_rho", pv_names[i]), TString::Format(";%s rho (cm);events/5 #mum", pv_names[i]), 200, 0, 0.1);
      h_pv_phi[i] = fs->make<TH1F>(TString::Format("h_%s_phi", pv_names[i]), TString::Format(";%s #phi (rad);events/.063", pv_names[i]), 100, -3.1416, 3.1416);
      h_pv_ntracks[i] = fs->make<TH1F>(TString::Format("h_%s_ntracks", pv_names[i]), TString::Format(";%s # of tracks in primary vertex;events", pv_names[i]), 200, 0, 200);
      h_pv_sumpt2[i] = fs->make<TH1F>(TString::Format("h_%s_sumpt2", pv_names[i]), TString::Format(";%s #Sigma p_{T}^{2} (GeV^{2});events/10 GeV^{2}", pv_names[i]), 200, 0, 2000);
    }
  }

  if (jets_src.label() != "") {
    h_jets_n = fs->make<TH1F>("h_jets_n", ";# of jets;events", 20, 0, 20);
    h_jets_pt = fs->make<TH1F>("h_jets_pt", ";jet pt;number of jets", 100, 0, 500);
    h_jets_eta = fs->make<TH1F>("h_jets_eta", ";jet eta;number of jets", 50, -4, 4);
    h_jets_phi = fs->make<TH1F>("h_jets_phi", ";jet phi;number of jets", 50, -3.15, 3.15);

    const char* b_wpnames[NBDISC] = {"JP", "CSV"};
    for (int i = 0; i < NBDISC; ++i) {
      for (int j = 0; j < 3; ++j) {
        h_bjets_n[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s%s_n", b_wpnames[i], lmt_ex[j]), TString::Format(";# of %s %s bjets;events", b_wpnames[i], lmt_ex[j]), 20, 0, 20);
        h_bjets_pt[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s%s_pt", b_wpnames[i], lmt_ex[j]), TString::Format(";%s %s bjet pt;number of bjets", b_wpnames[i], lmt_ex[j]), 100, 0, 500);
        h_bjets_eta[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s%s_eta", b_wpnames[i], lmt_ex[j]), TString::Format(";%s %s bjet eta;number of bjets", b_wpnames[i], lmt_ex[j]), 50, -4, 4);
        h_bjets_phi[i][j] = fs->make<TH1F>(TString::Format("h_bjets_%s%s_phi", b_wpnames[i], lmt_ex[j]), TString::Format(";%s %s bjet phi;number of bjets", b_wpnames[i], lmt_ex[j]), 50, -3.15, 3.15);
      }
    }
  }
}

void MFVEventHistos::analyze(const edm::Event& event, const edm::EventSetup&) {
  edm::Handle<MFVEvent> mevent;
  event.getByLabel(mfv_event_src, mevent);

  edm::Handle<double> weight;
  event.getByLabel(weight_src, weight);
  const double w = *weight;
  h_w->Fill(w);

  const double bsx = force_bs.size() ? force_bs[0] : mevent->bsx;
  const double bsy = force_bs.size() ? force_bs[1] : mevent->bsy;
  const double bsz = force_bs.size() ? force_bs[2] : mevent->bsz;

  //////////////////////////////////////////////////////////////////////////////

  h_gen_decay->Fill(mevent->gen_decay_type[0], mevent->gen_decay_type[1], w);
  h_gen_partons_in_acc->Fill(mevent->gen_partons_in_acc, w);

  h_minlspdist2d->Fill(mevent->minlspdist2d(), w);
  h_lspdist2d->Fill(mevent->lspdist2d(), w);
  h_lspdist3d->Fill(mevent->lspdist3d(), w);

  //////////////////////////////////////////////////////////////////////////////

  bool pass_trigger[mfv::n_trigger_paths] = { 0 };

  if (re_trigger) {
    TriggerHelper trig_helper(event, edm::InputTag("TriggerResults", "", "HLT"));
    mfv::trigger_decision(trig_helper, pass_trigger);
  }

  for (int i = 0; i < mfv::n_trigger_paths; ++i)
    h_pass_trigger[i]->Fill((re_trigger ? pass_trigger : mevent->pass_trigger)[i], w);

  for (int i = 0; i < mfv::n_clean_paths; ++i)
    h_pass_clean[i]->Fill(mevent->pass_clean[i], w);

  bool pass_clean_all = !(mevent->pass_clean[11]);
  int clean_all[12] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 19};
  for (int i = 0; i < 12; ++i) {
    pass_clean_all = pass_clean_all && mevent->pass_clean[clean_all[i]];
  }
  h_pass_clean_all->Fill(pass_clean_all, w);

  h_passoldskim->Fill(mevent->passoldskim);

  //////////////////////////////////////////////////////////////////////////////

  h_npfjets->Fill(mevent->npfjets, w);
  h_pfjetpt4->Fill(mevent->pfjetpt4, w);
  h_pfjetpt5->Fill(mevent->pfjetpt5, w);
  h_pfjetpt6->Fill(mevent->pfjetpt6, w);

  h_npu->Fill(mevent->npu, w);

  h_bsx->Fill(bsx, w);
  h_bsy->Fill(bsy, w);
  h_bsz->Fill(bsz, w);
  h_bsphi->Fill(atan2(bsy, bsx), w);

  h_npv->Fill(mevent->npv, w);
  h_pvx->Fill(mevent->pvx - bsx, w);
  h_pvy->Fill(mevent->pvy - bsy, w);
  h_pvz->Fill(mevent->pvz - bsz, w);
  h_pvphi->Fill(atan2(mevent->pvy - bsy, mevent->pvx - bsx), w);
  h_pvntracks->Fill(mevent->pv_ntracks, w);
  h_pvsumpt2->Fill(mevent->pv_sumpt2, w);
  h_pvrho->Fill(mevent->pv_rho(), w);

  h_njets->Fill(mevent->njets(), w);
  for (int i = 0; i < 3; ++i)
    h_njetsnopu[i]->Fill(mevent->njetsnopu(i), w);
  h_jetpt4->Fill(mevent->jetpt4(), w);
  h_jetpt5->Fill(mevent->jetpt5(), w);
  h_jetpt6->Fill(mevent->jetpt6(), w);
  h_jet_sum_ht->Fill(mevent->jet_sum_ht(), w);
  for (size_t ijet = 0; ijet < mevent->jet_id.size(); ++ijet) {
    h_jetphi->Fill(mevent->jet_phi[ijet]);
    for (size_t jjet = ijet+1; jjet < mevent->jet_id.size(); ++jjet) {
      h_jetpairdphi->Fill(reco::deltaPhi(mevent->jet_phi[ijet], mevent->jet_phi[jjet]));
    }
  }

  if (mevent->njets() > 0) {
    double rjetphi = 0;
    double rand = gRandom->Rndm();
    double sumpt = 0;
    for (size_t ijet = 0; ijet < mevent->jet_id.size(); ++ijet) {
      sumpt += mevent->jet_pt[ijet];
      if (rand < sumpt/mevent->jet_sum_ht()) {
        rjetphi = mevent->jet_phi[ijet];
        break;
      }
    }
    double rdphi = gRandom->Gaus(1.57, 0.4);

    double vtx0_phi = 0;
    if (gRandom->Rndm() < 0.5) {
      vtx0_phi = rjetphi - rdphi;
    } else {
      vtx0_phi = rjetphi + rdphi;
    }

    rjetphi = 0;
    rand = gRandom->Rndm();
    sumpt = 0;
    for (size_t ijet = 0; ijet < mevent->jet_id.size(); ++ijet) {
      sumpt += mevent->jet_pt[ijet];
      if (rand < sumpt/mevent->jet_sum_ht()) {
        rjetphi = mevent->jet_phi[ijet];
        break;
      }
    }
    rdphi = gRandom->Gaus(1.57, 0.4);

    double vtx1_phi = 0;
    if (gRandom->Rndm() < 0.5) {
      vtx1_phi = rjetphi - rdphi;
    } else {
      vtx1_phi = rjetphi + rdphi;
    }

    double dphi = reco::deltaPhi(vtx0_phi, vtx1_phi);
    //double vtx0_dist = h_bs2ddist1v->GetRandom();
    //double vtx1_dist = h_bs2ddist1v->GetRandom();
    double vtx0_dist = gRandom->Exp(0.005);
    double vtx1_dist = gRandom->Exp(0.005);

    h_sv0phi->Fill(reco::deltaPhi(vtx0_phi, 0.0));
    h_sv1phi->Fill(reco::deltaPhi(vtx1_phi, 0.0));
    for (size_t ijet = 0; ijet < mevent->jet_id.size(); ++ijet) {
      h_sv0jetdphi->Fill(reco::deltaPhi(vtx0_phi, mevent->jet_phi[ijet]));
      h_sv1jetdphi->Fill(reco::deltaPhi(vtx1_phi, mevent->jet_phi[ijet]));
    }
    h_svpairdphi->Fill(dphi);

    h_sv0bs2ddist->Fill(vtx0_dist);
    h_sv1bs2ddist->Fill(vtx1_dist);
    double svdist = sqrt(vtx0_dist*vtx0_dist + vtx1_dist*vtx1_dist - 2*vtx0_dist*vtx1_dist*cos(fabs(dphi)));
    h_svpairdist->Fill(svdist);
    h_svdist_dphi->Fill(dphi, svdist);
    h_svdist_bs2ddist0->Fill(vtx0_dist, svdist);
    h_svdist_bs2ddist1->Fill(vtx1_dist, svdist);
    h_bs2ddist1_bs2ddist0->Fill(vtx0_dist, vtx1_dist);

    if (TMath::Erf((svdist - 0.028)/0.005) > gRandom->Uniform(-1,1)) {
      h_svpairdphi_cut->Fill(dphi);
      h_svpairdist_cut->Fill(svdist);
    }
  }

  h_metx->Fill(mevent->metx);
  h_mety->Fill(mevent->mety);
  h_metsig->Fill(mevent->metsig);
  h_met->Fill(mevent->met());
  h_metphi->Fill(mevent->metphi());
  h_metdphimin->Fill(mevent->metdphimin);

  std::vector<double> bjets_eta[3][2];
  std::vector<double> bjets_phi[3][2];
  std::vector<double> muons_eta[3];
  std::vector<double> muons_phi[3];
  for (int i = 0; i < 3; ++i) {
    h_nbtags[i]->Fill(mevent->nbtags(i), w);
    h_nmuons[i]->Fill(mevent->nmu(i), w);
    h_nelectrons[i]->Fill(mevent->nel(i), w);
    h_nleptons[i]->Fill(mevent->nlep(i), w);

    for (size_t ijet = 0; ijet < mevent->jet_id.size(); ++ijet) {
      if (((mevent->jet_id[ijet] >> 2) & 3) >= i + 1) {
        for (int j = 0; j < 2; ++j) {
          if (j==1 && mevent->jet_pt[ijet] < 50) continue;
          bjets_eta[i][j].push_back(mevent->jet_eta[ijet]);
          bjets_phi[i][j].push_back(mevent->jet_phi[ijet]);
        }
      }
    }
    for (int j = 0; j < 2; ++j) {
      if (bjets_phi[i][j].size() == 2) {
        double dphi = reco::deltaPhi(bjets_phi[i][j][0], bjets_phi[i][j][1]);
        double deta = bjets_eta[i][j][0] - bjets_eta[i][j][1];
        double avgeta = (bjets_eta[i][j][0] + bjets_eta[i][j][1]) / 2;
        double dR = reco::deltaR(bjets_eta[i][j][0], bjets_phi[i][j][0], bjets_eta[i][j][1], bjets_phi[i][j][1]);
        h_bjets_absdphi[i][j]->Fill(fabs(dphi));
        h_bjets_dphi[i][j]->Fill(dphi);
        h_bjets_deta[i][j]->Fill(deta);
        h_bjets_deta_dphi[i][j]->Fill(dphi, deta);
        h_bjets_avgeta[i][j]->Fill(avgeta);
        h_bjets_avgeta_dphi[i][j]->Fill(dphi, avgeta);
        h_bjets_dR[i][j]->Fill(dR);
        h_bjets_dR_dphi[i][j]->Fill(dphi, dR);
      }
    }

    for (size_t ilep = 0; ilep < mevent->lep_id.size(); ++ilep) {
      if ((mevent->lep_id[ilep] & 1) == 0 && (mevent->lep_id[ilep] & (1 << (i+1)))) {
        muons_eta[i].push_back(mevent->lep_eta[ilep]);
        muons_phi[i].push_back(mevent->lep_phi[ilep]);
      }
    }
    if (muons_phi[i].size() == 2) {
      double dphi = reco::deltaPhi(muons_phi[i][0], muons_phi[i][1]);
      double deta = muons_eta[i][0] - muons_eta[i][1];
      double avgeta = (muons_eta[i][0] + muons_eta[i][1]) / 2;
      double dR = reco::deltaR(muons_eta[i][0], muons_phi[i][0], muons_eta[i][1], muons_phi[i][1]);
      h_muons_absdphi[i]->Fill(fabs(dphi));
      h_muons_dphi[i]->Fill(dphi);
      h_muons_deta[i]->Fill(deta);
      h_muons_deta_dphi[i]->Fill(dphi, deta);
      h_muons_avgeta[i]->Fill(avgeta);
      h_muons_avgeta_dphi[i]->Fill(dphi, avgeta);
      h_muons_dR[i]->Fill(dR);
      h_muons_dR_dphi[i]->Fill(dphi, dR);
    }
  }

  //////////////////////////////////////////////////////////////////////////////

  edm::Handle<reco::VertexCollection> primary_vertices;
  if (primary_vertex_src.label() != "") {
    event.getByLabel(primary_vertex_src, primary_vertices);

    const int npv = int(primary_vertices->size());
    h_pv_n->Fill(npv, w);

    const reco::Vertex& pv0 = primary_vertices->at(0);
    double absdz = 100000;
    int ipvdz = 0;
    for (int ipv = 1; ipv < npv; ++ipv) {
      const reco::Vertex& pv = primary_vertices->at(ipv);
      if (fabs(pv.z() - pv0.z()) < absdz) {
        absdz = fabs(pv.z() - pv0.z());
        ipvdz = ipv;
      }
    }

    for (int ipv = 1; ipv < npv; ++ipv) {
      const reco::Vertex& pv = primary_vertices->at(ipv);
      double sumpt2 = 0;
      for (auto trki = pv.tracks_begin(), trke = pv.tracks_end(); trki != trke; ++trki) {
        double trkpt = (*trki)->pt();
        sumpt2 += trkpt * trkpt;
      }

      const int isumpt2 = ipv == 1 ? 0 : 1;
      h_pv_x[isumpt2]->Fill(pv.x() - bsx, w);
      h_pv_y[isumpt2]->Fill(pv.y() - bsy, w);
      h_pv_z[isumpt2]->Fill(pv.z() - bsz, w);
      h_pv_rho[isumpt2]->Fill(sqrt((pv.x() - bsx) * (pv.x() - bsx) + (pv.y() - bsy) * (pv.y() - bsy)), w);
      h_pv_phi[isumpt2]->Fill(atan2(pv.y() - bsy, pv.x() - bsx), w);
      h_pv_ntracks[isumpt2]->Fill(pv.nTracks(), w);
      h_pv_sumpt2[isumpt2]->Fill(sumpt2, w);

      const int iabsdz = ipv == ipvdz ? 2 : 3;
      h_pv_x[iabsdz]->Fill(pv.x() - bsx, w);
      h_pv_y[iabsdz]->Fill(pv.y() - bsy, w);
      h_pv_z[iabsdz]->Fill(pv.z() - bsz, w);
      h_pv_rho[iabsdz]->Fill(sqrt((pv.x() - bsx) * (pv.x() - bsx) + (pv.y() - bsy) * (pv.y() - bsy)), w);
      h_pv_phi[iabsdz]->Fill(atan2(pv.y() - bsy, pv.x() - bsx), w);
      h_pv_ntracks[iabsdz]->Fill(pv.nTracks(), w);
      h_pv_sumpt2[iabsdz]->Fill(sumpt2, w);
    }
  }

  //////////////////////////////////////////////////////////////////////////////

  edm::Handle<pat::JetCollection> jets;
  if (jets_src.label() != "") {
    event.getByLabel(jets_src, jets);

    const int njets = int(jets->size());
    h_jets_n->Fill(njets, w);

    const char* b_discriminators[NBDISC] = {"jetProbabilityBJetTags", "combinedSecondaryVertexBJetTags"};
    const double b_discriminator_mins[NBDISC][3] = {{0.275, 0.545, 0.790}, {0.244, 0.679, 0.898}};
    int nbjets[NBDISC][3] = {{0, 0, 0}, {0, 0, 0}};
    for (int i = 0; i < njets; ++i) {
      const pat::Jet& jet = jets->at(i);
      h_jets_pt->Fill(jet.pt(), w);
      h_jets_eta->Fill(jet.eta(), w);
      h_jets_phi->Fill(jet.phi(), w);
      for (int j = 0; j < NBDISC; ++j) {
        for (int k = 0; k < 3; ++k) {
          if (jet.bDiscriminator(b_discriminators[j]) > b_discriminator_mins[j][k]) {
            nbjets[j][k] += 1;
            h_bjets_pt[j][k]->Fill(jet.pt(), w);
            h_bjets_eta[j][k]->Fill(jet.eta(), w);
            h_bjets_phi[j][k]->Fill(jet.phi(), w);
          }
        }
      }
    }
    for (int j = 0; j < NBDISC; ++j) {
      for (int k = 0; k < 3; ++k) {
        h_bjets_n[j][k]->Fill(nbjets[j][k], w);
      }
    }
  }
}

DEFINE_FWK_MODULE(MFVEventHistos);
