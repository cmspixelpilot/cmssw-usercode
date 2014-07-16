#include "Templates.h"

#include <cmath>
#include "TH1D.h"
#include "VAException.h"

namespace mfv {
  const int Template::nbins = 20000;
  const double Template::min_val = 0;
  const double Template::max_val = 10;
  const double Template::bin_width = (Template::max_val - Template::min_val) / Template::nbins;
  const int Template::max_npars = 3;

  std::vector<double> Template::binning() {
    std::vector<double> bins;
    for (int i = 0; i < 20; ++i)
      bins.push_back(i * 0.01);
    bins.push_back(0.2);
    bins.push_back(0.4);
    bins.push_back(0.6);
    bins.push_back(1);
    bins.push_back(3);
    return bins;
  }

  TH1D* Template::hist_with_binning(const char* name, const char* title) {
    std::vector<double> bins = binning();
    return new TH1D(name, title, bins.size()-1, &bins[0]);
  }

  TH1D* Template::finalize_binning(TH1D* h) {
    std::vector<double> bins = binning();
    TH1D* hh = (TH1D*)h->Rebin(bins.size()-1, TString::Format("%s_rebinned", h->GetName()), &bins[0]);
    const int nb = hh->GetNbinsX();
    const double l  = hh->GetBinContent(nb);
    const double le = hh->GetBinError  (nb);
    const double o  = hh->GetBinContent(nb+1);
    const double oe = hh->GetBinError  (nb+1);
    hh->SetBinContent(nb, l + o);
    hh->SetBinError  (nb, sqrt(le*le + oe*oe));
    hh->SetBinContent(nb+1, 0);
    hh->SetBinError  (nb+1, 0);
    return hh;
  }

  TH1D* Template::finalize_template(TH1D* h) {
    TH1D* hh = finalize_binning(h);
    hh->Scale(1./hh->Integral());
    return hh;
  }

  //////////////////////////////////////////////////////////////////////////////

  PhiShiftTemplate::PhiShiftTemplate(int i_, TH1D* h_, const double phi_exp_, const double shift_)
    : Template(i_, h_),
      phi_exp(phi_exp_),
      shift(shift_)
  {
    pars.push_back(phi_exp);
    pars.push_back(shift);
  }

  double PhiShiftTemplate::chi2() const {
    return 0; // pow(phi_exp - 1.7, 2)/0.7
  }

  std::string PhiShiftTemplate::name() const {
    char buf[128];
    snprintf(buf, 128, "phishift%04i", i);
    return std::string(buf);
  }

  std::string PhiShiftTemplate::title() const {
    char buf[128];
    snprintf(buf, 128, "phi_exp = %f, shift = %g", phi_exp, shift);
    return std::string(buf);
  }

  double PhiShiftTemplate::par(size_t w) const {
    if (w == 0)
      return phi_exp;
    else if (w == 1)
      return shift;
    else
      return 0.;
  }

  //////////////////////////////////////////////////////////////////////////////

  ClearedJetsTemplate::ClearedJetsTemplate(int i_, TH1D* h_)
    : Template(i_, h_)
  {
  }

  //////////////////////////////////////////////////////////////////////////////

  TemplateInterpolator::TemplateInterpolator(Templates* templates_, int n_bins_,
                                             const std::vector<TemplatePar>& par_infos_,
                                             std::vector<double>& a_)
    : templates(templates_),
      n_bins(n_bins_),
      n_pars(templates->at(0)->npars()),
      par_infos(par_infos_),
      a(a_)
  {
    if (n_pars != 2)
      jmt::vthrow("only n_pars = 2 implemented in TemplateInterpolator"); // JMTBAD

    if (int(par_infos.size()) != n_pars)
      jmt::vthrow("TemplateInterpolator:: par_infos size %lu != n_pars %i", par_infos.size(), n_pars);

    for (Template* t : *templates)
      if (int(t->npars()) != n_pars)
        jmt::vthrow("template mismatch in TemplateInterpolator");

    a.resize(n_bins+2);
    int nR = 0;
    int nQ = 1;
    for (int i = 0; i < n_pars; ++i) {
      nR += 2*nQ;
      nQ *= 2;
    }

    R.resize(nR);
    for (std::vector<double>& v : R)
      v.resize(n_bins+2);
    Q.resize(nQ);
  }

  int TemplateInterpolator::i_par(int i, double par) const {
    int ret((par - par_infos[i].start) / par_infos[i].step);
    if (ret <= 0)
      return 0;
    else if (ret >= par_infos[i].nsteps)
      return par_infos[i].nsteps - 1;
    else
      return ret;
  }

  int TemplateInterpolator::i_Q(const std::vector<double>& pars) const {
    std::vector<int> ipars;
    int ret = 0;
    int mult = 1;
    //printf("\niq %f %f\n", pars[0], pars[1]);
    for (int i = n_pars-1; i >= 0; --i) {
      int ip = i_par(i, pars[i]);
      ret += ip * mult;
      mult *= par_infos[i].nsteps;
      //printf("i %i ip %i ret %i mult %i\n", i, ip, ret, mult);
    }
    return ret;
  }

  Template* TemplateInterpolator::get_Q(const std::vector<double>& pars) const {
    return (*templates)[i_Q(pars)];
  }

  void TemplateInterpolator::interpolate(const std::vector<double>& pars, std::vector<double>* a_p) {
    if (int(pars.size()) != n_pars)
      jmt::vthrow("TemplateInterpolator::interpolate: pars size %lu != n_pars %i", pars.size(), n_pars);

    if (a_p == 0)
      a_p = &a;

    //std::vector<int> ipars;
    //for (int i = 0; i < n_pars; ++i)
    //  ipars = ipar(i, pars[i]);

    const int i_par0 = i_par(0, pars[0]);
    const int i_par1 = i_par(1, pars[1]);
    const int i_par0_p1 = i_par0 == par_infos[0].nsteps - 1 ? i_par0 : i_par0 + 1;
    const int i_par1_p1 = i_par1 == par_infos[1].nsteps - 1 ? i_par1 : i_par1 + 1;
    const int n_par1 = par_infos[1].nsteps;

    Q[0] = (*templates)[n_par1 * i_par0    + i_par1   ];
    Q[1] = (*templates)[n_par1 * i_par0    + i_par1_p1];
    Q[2] = (*templates)[n_par1 * i_par0_p1 + i_par1   ];
    Q[3] = (*templates)[n_par1 * i_par0_p1 + i_par1_p1];

    //    printf("interpolate: %f %f\n", pars[0], pars[1]);
    //    for (int i = 0; i < 4; ++i)
    //      printf("Q%i: %s\n", i, Q[i]->title().c_str());

    if (i_par0 == i_par0_p1 && i_par1 == i_par1_p1) {
      for (int ibin = 1; ibin <= n_bins; ++ibin)
        (*a_p)[ibin] = Q[0]->h->GetBinContent(ibin);
    }
    else if (i_par0 == i_par0_p1) {
      const double d = Q[1]->par(1) - Q[0]->par(1);
      const double f = (Q[1]->par(1) - pars[1])/d;
      for (int ibin = 1; ibin <= n_bins; ++ibin)
        (*a_p)[ibin] = f * Q[0]->h->GetBinContent(ibin) + (1-f) * Q[1]->h->GetBinContent(ibin);
    }
    else if (i_par1 == i_par1_p1) {
      const double d = Q[2]->par(0) - Q[0]->par(0);
      const double f = (Q[2]->par(0) - pars[0])/d;
      for (int ibin = 1; ibin <= n_bins; ++ibin)
        (*a_p)[ibin] = f * Q[0]->h->GetBinContent(ibin) + (1-f) * Q[2]->h->GetBinContent(ibin);
    }
    else {
      for (int i = 0; i < 2; ++i) {
        const double d = Q[2+i]->par(0) - Q[i]->par(0);
        const double f = (Q[2+i]->par(0) - pars[0])/d;
        //printf("R[%i] d %f f %f\n", i, d, f);
        for (int ibin = 1; ibin <= n_bins; ++ibin) {
          R[i][ibin] = f * Q[i]->h->GetBinContent(ibin) + (1-f) * Q[2+i]->h->GetBinContent(ibin);
          //printf("   Q[%i].hc %f  Q[%i].hc %f  R[%i][%i] %f\n", i, Q[i]->h->GetBinContent(ibin), 2+i, Q[2+i]->h->GetBinContent(ibin), i, ibin, R[i][ibin]);
        }
      }

      const double d = Q[1]->par(1) - Q[0]->par(1);
      const double f = (Q[1]->par(1) - pars[1])/d;
      //printf("a d %f f %f\n", d, f);
      for (int ibin = 1; ibin <= n_bins; ++ibin) {
        (*a_p)[ibin] = f * R[0][ibin] + (1-f) * R[1][ibin];
        //printf("   R[0][%i] %f R[1][%i] %f  a[%i] %f\n", ibin, R[0][ibin], ibin, R[1][ibin], ibin, (*a_p)[ibin]);
      }
    }
  }
}
