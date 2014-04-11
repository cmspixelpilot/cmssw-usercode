#ifndef JMTucker_MFVNeutralinoFormats_interface_VertexAux_h
#define JMTucker_MFVNeutralinoFormats_interface_VertexAux_h

#include <vector>
#include "TLorentzVector.h"
#include "JMTucker/MFVNeutralinoFormats/interface/JetVertexAssociation.h"

struct MFVVertexAux {
  typedef unsigned char uchar;
  typedef unsigned short ushort;
  typedef unsigned int uint;

  MFVVertexAux() {
    which = ntracks = nbadtracks = ntracksptgt3 = ntracksptgt5 = ntracksptgt10 = trackminnhits = trackmaxnhits = sumnhitsbehind = maxnhitsbehind = ntrackssharedwpv = ntrackssharedwpvs = npvswtracksshared = bs2dcompatscss = pv2dcompatscss = pv3dcompatscss = 0;
    x = y = z = cxx = cxy = cxz = cyy = cyz = czz = chi2 = ndof = sumpt2 = mintrackpt = maxtrackpt = maxm1trackpt = maxm2trackpt = drmin = drmax = dravg = drrms = dravgw = drrmsw = gen2ddist = gen2derr = gen3ddist = gen3derr = bs2dcompat = bs2ddist = bs2derr = bs3ddist = pv2dcompat = pv2ddist = pv2derr = pv3dcompat = pv3ddist = pv3derr = trackptavg = trackptrms = trackdxymin = trackdxymax = trackdxyavg = trackdxyrms = trackdzmin = trackdzmax = trackdzavg = trackdzrms = trackpterrmin = trackpterrmax = trackpterravg = trackpterrrms = trackdxyerrmin = trackdxyerrmax = trackdxyerravg = trackdxyerrrms = trackdzerrmin = trackdzerrmax = trackdzerravg = trackdzerrrms = trackpairmassmin = trackpairmassmax = trackpairmassavg = trackpairmassrms = tracktripmassmin = tracktripmassmax = tracktripmassavg = tracktripmassrms = trackquadmassmin = trackquadmassmax = trackquadmassavg = trackquadmassrms = jetpairdrmin = jetpairdrmax = jetpairdravg = jetpairdrrms = costhtkmomvtxdispmin = costhtkmomvtxdispmax = costhtkmomvtxdispavg = costhtkmomvtxdisprms = costhjetmomvtxdispmin = costhjetmomvtxdispmax = costhjetmomvtxdispavg = costhjetmomvtxdisprms = 0;
    for (int i = 0; i < mfv::NJetsByUse; ++i)
      njets[i] = 0;
    for (int i = 0; i < mfv::NMomenta; ++i)
      pt[i] = eta[i] = phi[i] = mass[i] = costhmombs[i] = costhmompv2d[i] = costhmompv3d[i] = missdistpv[i] = missdistpverr[i] = 0;
  }

  uchar which;
  std::vector<uchar> which_lep; // electrons have 7th bit set

  float x;
  float y;
  float z;

  float cxx;
  float cxy;
  float cxz;
  float cyy;
  float cyz;
  float czz;

  float chi2;
  float ndof;

  uchar njets[mfv::NJetsByUse];

  float pt  [mfv::NMomenta];
  float eta [mfv::NMomenta];
  float phi [mfv::NMomenta];
  float mass[mfv::NMomenta];

  TLorentzVector p4(int w=0) const {
    TLorentzVector v;
    v.SetPtEtaPhiM(pt[w], eta[w], phi[w], mass[w]);
    return v;
  }

  uchar ntracks;
  uchar nbadtracks;

  uchar ntracksptgt3;
  uchar ntracksptgt5;
  uchar ntracksptgt10;

  uchar trackminnhits;
  uchar trackmaxnhits;

  float sumpt2;

  uchar sumnhitsbehind;
  uchar maxnhitsbehind;

  uchar ntrackssharedwpv;
  uchar ntrackssharedwpvs;
  uchar npvswtracksshared;
  uchar pvmosttracksshared;

  float mintrackpt;
  float maxtrackpt;
  float maxm1trackpt;
  float maxm2trackpt;

  float trackptavg;
  float trackptrms;

  float trackdxymin;
  float trackdxymax;
  float trackdxyavg;
  float trackdxyrms;

  float trackdzmin;
  float trackdzmax;
  float trackdzavg;
  float trackdzrms;

  float trackpterrmin;
  float trackpterrmax;
  float trackpterravg;
  float trackpterrrms;

  float trackdxyerrmin;
  float trackdxyerrmax;
  float trackdxyerravg;
  float trackdxyerrrms;

  float trackdzerrmin;
  float trackdzerrmax;
  float trackdzerravg;
  float trackdzerrrms;

  float trackpairdetamin;
  float trackpairdetamax;
  float trackpairdetaavg;
  float trackpairdetarms;

  float drmin; // JMTBAD trackpairdrmin
  float drmax;
  float dravg;
  float drrms;
  float dravgw;
  float drrmsw;

  float trackpairmassmin;
  float trackpairmassmax;
  float trackpairmassavg;
  float trackpairmassrms;

  float tracktripmassmin;
  float tracktripmassmax;
  float tracktripmassavg;
  float tracktripmassrms;

  float trackquadmassmin;
  float trackquadmassmax;
  float trackquadmassavg;
  float trackquadmassrms;

  float jetpairdetamin;
  float jetpairdetamax;
  float jetpairdetaavg;
  float jetpairdetarms;

  float jetpairdrmin;
  float jetpairdrmax;
  float jetpairdravg;
  float jetpairdrrms;

  float costhtkmomvtxdispmin;
  float costhtkmomvtxdispmax;
  float costhtkmomvtxdispavg;
  float costhtkmomvtxdisprms;

  float costhjetmomvtxdispmin;
  float costhjetmomvtxdispmax;
  float costhjetmomvtxdispavg;
  float costhjetmomvtxdisprms;

  float sig(float val, float err) const {
    return err <= 0 ? 0 : val/err;
  }

  float gen2ddist;
  float gen2derr;
  float gen2dsig() const { return sig(gen2ddist, gen2derr); }

  float gen3ddist;
  float gen3derr;
  float gen3dsig() const { return sig(gen3ddist, gen3derr); }

  uchar bs2dcompatscss;
  float bs2dcompat;
  float bs2ddist;
  float bs2derr;
  float bs2dsig() const { return sig(bs2ddist, bs2derr); }

  float bs3ddist;

  uchar pv2dcompatscss;
  float pv2dcompat;
  float pv2ddist;
  float pv2derr;
  float pv2dsig() const { return sig(pv2ddist, pv2derr); }

  uchar pv3dcompatscss;
  float pv3dcompat;
  float pv3ddist;
  float pv3derr;
  float pv3dsig() const { return sig(pv3ddist, pv3derr); }

  float pvdz() const { return sqrt(pv3ddist*pv3ddist - pv2ddist*pv2ddist); }
  float pvdzerr() const {
    // JMTBAD
    float z = pvdz();
    if (z == 0)
      return -1;
    return sqrt(pv3ddist*pv3ddist*pv3derr*pv3derr + pv2ddist*pv2ddist*pv2derr*pv2derr)/z;
  }
  float pvdzsig() const { return sig(pvdz(), pvdzerr()); }

  float costhmombs  [mfv::NMomenta];
  float costhmompv2d[mfv::NMomenta];
  float costhmompv3d[mfv::NMomenta];

  float missdistpv   [mfv::NMomenta];
  float missdistpverr[mfv::NMomenta];
  float missdistpvsig(int w) const { return sig(missdistpv[w], missdistpverr[w]); }
};

typedef std::vector<MFVVertexAux> MFVVertexAuxCollection;

#endif
