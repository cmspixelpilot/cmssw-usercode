#ifndef JMTucker_MFVNeutralino_One2Two_ROOTTools_h
#define JMTucker_MFVNeutralino_One2Two_ROOTTools_h

class TH1D;
class TGraphAsymmErrors;

namespace jmt {
  void divide_by_bin_width(TH1D* h);
  void cumulate(TH1D* h, const bool do_overflow);
  void set_root_style();
  TH1D* shift_hist(const TH1D* h, const int shift);
  TGraphAsymmErrors* poisson_intervalize(const TH1D* h, const bool zero_x=false, const bool include_zero_bins=false);
}

#endif
