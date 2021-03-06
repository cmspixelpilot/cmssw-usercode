#!/usr/bin/env python

import sys, os, glob
from JMTucker.Tools.ROOTTools import *
from JMTucker.Tools.CRABTools import *

set_style()
ROOT.TH1.AddDirectory(0)
ps = plot_saver('plots/MakeSamples_check_nevs', log=False, size=(500,300), canvas_margins=(0, 0.05, 0.05, 0))

dirs = crab_dirs_from_argv()
ndirs = len(dirs)
def nice(dir):
    d = os.path.basename(dir).replace('crab_', '')
    d = d.replace('mfv_neutralino_tau', '')
    t,m = d.split('um_M')
    t = t[:-2]
    m = m[:-2]
    d = 't%sM%s' % (t,m)
    return d

hns = 'gen reco ntuple minitree one two'.split()
statns = 'entries mean rms under over'.split()

hstats = []
for hn in hns:
    for hn2 in statns:
        h = ROOT.TH1F('h_%s_%s' % (hn, hn2), '', ndirs, 0, ndirs)
        h.SetLineWidth(2)
        h.SetStats(0)
        #h.SetMinimum(0)
        h.SetMarkerSize(1)
        h.SetMarkerStyle(1)
        for idir, dir in enumerate(dirs):
            h.GetXaxis().SetBinLabel(idir+1, nice(dir))
        hstats.append(h)
        exec '%s = h' % h.GetName()

for idir, dir in enumerate(dirs):
    print dir
    njobs = crab_get_njobs(dir)
    missing_stdouts = []
    missing_roots = []

    colors = (1,38,2,418,4,6)
    hs = []
    for hn, color in zip(hns, colors):
        h = ROOT.TH1F('%s' % hn, '', 205, 0, 205)
        h.SetLineColor(color)
        h.SetLineWidth(2)
        hs.append(h)
        exec 'h_%s = h' % hn

    for job in xrange(1, njobs+1):
        stdout = os.path.join(dir, 'res/CMSSW_%i.stdout' % job)
        if not os.path.isfile(stdout):
            missing_stdouts.append(job)
        else:
            nevs = []
            for line in open(stdout):
                if line.startswith('NEV'):
                    line = line.replace('\x1b[?1034h', '') # lol, only happens on some jobs = some sites?
                    try:
                        nev = int(line.split()[-1])
                    except ValueError:
                        raise RuntimeError('parsing problem for NEV for %s job %i: %r' % (dir, job, line))
                    nevs.append(nev)
            if len(nevs) != 4:
                raise RuntimeError('did not find 4 NEV lines for %s job %i' % (dir, job))

            for h,nev in zip(hs, nevs):
                h.Fill(nev)

        roots = glob.glob(os.path.join(dir, 'res/*_%i_*_???.root' % job))
        if len(roots) > 1:
            raise RuntimeError('more than one match for %s job %i: %r' % (dir, job, roots))
        elif len(roots) == 0:
            missing_roots.append(job)
        else:
            root = roots[0]
            f = ROOT.TFile(root)
            t = f.Get('mfvMiniTree/t')
            one, two = 0, 0
            for nvtx, in detree(t, 'nvtx'):
                if nvtx == 1:
                    one += 1
                elif nvtx == 2:
                    two += 1
                else:
                    raise RuntimeError('bad nvtx for %s job %i: %i' % (dir, job, nvtx))
            h_one.Fill(one)
            h_two.Fill(two)

    for i,h in enumerate(hs):
        if i == 0:
            h.Draw('hist')
        else:
            h.Draw('hist sames')
        ps.c.Update()
        move = (3-i%3, i/3)
        differentiate_stat_box(h, move, new_size=(0.27, 0.33), offset=(0.17, -0.03))

        hn = h.GetName()
        stats = get_hist_stats(h, fit=False)
        for statn in statns:
            hstat = eval('h_%s_%s' % (hn, statn))
            ve = stats[statn]
            if type(ve) == tuple:
                v,e = ve
            else:
                v,e = ve, 0.
            hstat.SetBinContent(idir+1, v)
            hstat.SetBinError  (idir+1, e)

    ps.save(nice(dir))

for hstat in hstats:
    hstat.Draw('text')
    ps.save(hstat.GetName())

