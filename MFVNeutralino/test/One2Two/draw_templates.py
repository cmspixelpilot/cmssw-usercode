#!/usr/bin/env python

from base import *

fn_pattern = 'trees/mfv*root'
plot_dir = 'plots/o2t_signal_templates'
binning = [0.02*i for i in xrange(5)] + [0.1, .15] # JMTBAD keep in sync with Templates.cc
last_bin_width = 5-.1
binning = array('d', binning)
nbins = len(binning) - 1
min_ntracks = 5

ps = plot_saver(plot_dir, size=(600,600))

fns = glob.glob(fn_pattern)
fns.sort()

hs = []

def scale(h):
    hint = h.Integral()
    nbins = h.GetNbinsX()
    for ibin in xrange(1, nbins+1):
        c = h.GetBinContent(ibin)
        ce = h.GetBinError(ibin)
        width = h.GetBinWidth(ibin) if ibin != nbins else last_bin_width
        scale = 1./hint/width
        h.SetBinContent(ibin, c  * scale)
        h.SetBinError  (ibin, ce * scale)

f = ROOT.TFile('mfvo2t_data.root')
h_bkg = f.Get('Fitter/seed00_toy-1/fit_results/h_bkg_sb_fit_nobb_nodiv_shortened')
h_bkg.SetStats(0)
h_bkg.SetLineWidth(2)
h_bkg.SetLineColor(1)
h_bkg.SetFillStyle(0)
h_bkg.Scale(1/h_bkg.Integral())
h_bkg.SetTitle(';d_{VV} (cm);frac. / bin width')
scale(h_bkg)
h_bkg.SetDirectory(0)
#h_bkg.GetYaxis().SetRangeUser(2e-5, 60)
hs.append(h_bkg)

masses = range(200, 1001, 200)
masses.insert(1, 300)
for mass in masses:
    colors = [2,3,4,6]
    titles = [
        '#tau = 100 #mum',
        '#tau = 300 #mum',
        '#tau = 1 mm',
        '#tau = 9.9 mm',
    ]
    leg = ROOT.TLegend(0.339, .610, .847, .871)
    leg.AddEntry(h_bkg, 'Bkg: #mu_{clear} = 320 #mum, #sigma_{clear} = 110 #mum', 'L')

    h_bkg.Draw('hist e')

    mass_name = 'M%04i' % mass

    for fn in fns:
        if mass_name not in fn:
            continue

        print fn
        sig_name = os.path.basename(fn).replace('.root','')
        f, t = get_f_t(fn, None)

        name = 'h_sig_ntk%i_%s' % (min_ntracks, sig_name)
        h = ROOT.TH1D(name, '', nbins, binning)
        h.SetDirectory(0)
        hs.append(h)
        x = detree(t, 'svdist', 'nvtx >= 2 && ntk0 >= %i && ntk1 >= %i' % (min_ntracks, min_ntracks), lambda x: (float(x[0]),))
        for (d,) in x:
            if d > .15:
                d = .149
            h.Fill(d)

        hint = h.Integral()
        for ibin in xrange(1, nbins+1):
            c = h.GetBinContent(ibin)
            v,lo,hi = clopper_pearson(c, hint)
            print '%s %10s %5i %.3f ; %.4f in [%.4f-%.4f] (-%.4f +%.4f)' % (mass_name, titles[0].replace('#tau = ',''), c, c**-0.5 if c > 0 else 0, v, lo, hi, v-lo, hi-v)

        scale(h)

        h.SetTitle(';d_{VV} (cm);frac. / bin width')
        h.SetStats(0)
        h.SetLineColor(colors.pop(0))
        h.SetLineWidth(2)
        h.Draw('same hist e')
        leg.AddEntry(h, 'Sig: ' + titles.pop(0), 'L')

    leg.SetBorderSize(0)
    leg.Draw()
    #ps.c.SetLogx()
    ps.save(mass_name, log=False)
    del leg
    ps.save(mass_name + '_log')
