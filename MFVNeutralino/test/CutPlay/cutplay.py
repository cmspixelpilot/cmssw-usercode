import os, sys
from JMTucker.Tools.BasicAnalyzer_cfg import cms, process
from JMTucker.Tools import SampleFiles

use_weights = True

process.source.fileNames = ['/store/user/tucker/mfv_neutralino_tau1000um_M0400/mfvntuple_v19/3b675468c132e35b291c67c94e024555/ntuple_1_1_1Ja.root']
process.TFileService.fileName = 'cutplay.root'

process.load('JMTucker.MFVNeutralino.VertexSelector_cfi')
vtx_sel = process.mfvSelectedVerticesTight

process.load('JMTucker.MFVNeutralino.AnalysisCuts_cfi')
ana_sel = process.mfvAnalysisCuts

def pize(f,sz):
    fmt = '%.' + str(sz) + 'f'
    return (fmt % f).replace('.','p').replace('-','n')

changes = []
changes.append(('nm1', '', ''))

if False:
    ana_sel.min_4th_jet_pt = 0
    for i in xrange(40, 200, 5):
        changes.append(('pf4ptX%i' % i, '', 'min_4th_jet_pt = %i' % i))
        changes.append(('pf5ptX%i' % i, '', 'min_5th_jet_pt = %i' % i))
        changes.append(('cl4ptX%i' % i, '', 'min_4th_calojet_pt = %i' % i))
        changes.append(('cl5ptX%i' % i, '', 'min_5th_calojet_pt = %i' % i))

for i in xrange(0,15):
    changes.append(('ntracksX%i'%i, 'min_ntracks = %i'%i, ''))

for i in xrange(0,10):
    changes.append(('ntracksptgt3X%i'%i, 'min_ntracksptgt3 = %i'%i, ''))

for i in xrange(0,10):
    changes.append(('ntracksptgt5X%i'%i, 'min_ntracksptgt5 = %i'%i, ''))

for i in xrange(0,10):
    changes.append(('ntracksptgt10X%i'%i, 'min_ntracksptgt10 = %i'%i, ''))

for i in xrange(0,6):
    changes.append(('njetsntksX%i'%i, 'min_njetsntks = %i'%i, ''))

for i in xrange(0,101,10):
    changes.append(('tkonlyptX%i'%i, 'min_tkonlypt = %i'%i, ''))

for i in xrange(1,7):
    changes.append(('abstkonlyetaX%s'%pize(0.5*i,1), 'max_abstkonlyeta = %f'%(0.5*i), ''))

for i in xrange(0,101,10):
    changes.append(('tkonlymassX%i'%i, 'min_tkonlymass = %i'%i, ''))

for i in xrange(0,201,20):
    changes.append(('jetsntkptX%i'%i, 'min_jetsntkpt = %i'%i, ''))

for i in xrange(0,201,20):
    changes.append(('jetsntkmassX%i'%i, 'min_jetsntkmass = %i'%i, ''))

for i in xrange(0,201,20):
    changes.append(('tksjetsntkptX%i'%i, 'min_tksjetsntkpt = %i'%i, ''))

for i in xrange(0,201,20):
    changes.append(('tksjetsntkmassX%i'%i, 'min_tksjetsntkmass = %i'%i, ''))

for i in xrange(-10,10):
    changes.append(('costhtkonlymombsX%s'%pize(0.1*i,1), 'min_costhtkonlymombs = %f'%(0.1*i), ''))

for i in xrange(0,51,5):
    changes.append(('missdisttkonlypvsigX%i'%i, 'min_missdisttkonlypvsig = %i'%i, ''))

for i in xrange(0,301,25):
    changes.append(('sumpt2X%i'%i, 'min_sumpt2 = %i'%i, ''))

for i in xrange(0,31,2):
    changes.append(('maxtrackptX%i'%i, 'min_maxtrackpt = %i'%i, ''))

for i in xrange(0,31,2):
    changes.append(('maxm1trackptX%i'%i, 'min_maxm1trackpt = %i'%i, ''))

for i in xrange(0,31,2):
    changes.append(('maxm2trackptX%i'%i, 'min_maxm2trackpt = %i'%i, ''))

for i in xrange(0,25):
    changes.append(('trackdxyerrminX%s'%pize(0.0004*i,4), 'max_trackdxyerrmin = %f'%(0.0004*i), ''))

for i in xrange(0,25):
    changes.append(('trackdxyerrmaxX%s'%pize(0.08*i,2), 'max_trackdxyerrmax = %f'%(0.08*i), ''))

for i in xrange(0,25):
    changes.append(('trackdxyerravgX%s'%pize(0.004*i,3), 'max_trackdxyerravg = %f'%(0.004*i), ''))

for i in xrange(0,25):
    changes.append(('trackdxyerrrmsX%s'%pize(0.004*i,3), 'max_trackdxyerrrms = %f'%(0.004*i), ''))

for i in xrange(0,25):
    changes.append(('trackdzerrminX%s'%pize(0.0004*i,4), 'max_trackdzerrmin = %f'%(0.0004*i), ''))

for i in xrange(0,25):
    changes.append(('trackdzerrmaxX%s'%pize(0.08*i,2), 'max_trackdzerrmax = %f'%(0.08*i), ''))

for i in xrange(0,25):
    changes.append(('trackdzerravgX%s'%pize(0.004*i,3), 'max_trackdzerravg = %f'%(0.004*i), ''))

for i in xrange(0,25):
    changes.append(('trackdzerrrmsX%s'%pize(0.004*i,3), 'max_trackdzerrrms = %f'%(0.004*i), ''))

for i in xrange(0,20):
    changes.append(('drminX%s'%pize(0.05*i,2), 'max_drmin = %f'%(0.05*i), ''))

for i in xrange(4,28):
    changes.append(('drmaxX%s'%pize(0.25*i,2), 'max_drmax = %f'%(0.25*i), ''))

for i in xrange(0,20):
    changes.append(('mindrmaxX%s'%pize(0.1*i,1), 'min_drmax = %f'%(0.1*i),''))

for i in xrange(0,25):
    changes.append(('jetpairdrminX%s'%pize(0.2*i,1), 'max_jetpairdrmin = %f'%(0.2*i), ''))

for i in xrange(0,20):
    changes.append(('jetpairdrmaxX%s'%pize(0.2*i,1), 'max_jetpairdrmax = %f'%(0.2*i), ''))

for i in xrange(0,20):
    changes.append(('bs2ddistX%s'%pize(0.002*i,3), 'min_bs2ddist = %f'%(0.002*i), ''))

for i in xrange(15,41):
    changes.append(('maxbs2ddistX%s'%pize(0.1*i,1), 'max_bs2ddist = %f'%(0.1*i), ''))

for i in xrange(0,50):
    changes.append(('bs2derrX%s'%pize(0.0005*i,4), 'max_bs2derr = %f'%(0.0005*i), ''))

for i in xrange(0,40,2):
    changes.append(('bs2dsigX%i'%i, 'min_bs2dsig = %i'%i, ''))

for i in xrange(250,1001,50):
    changes.append(('sumhtX%i'%i, '', 'min_sumht = %i'%i))

for i in xrange(0,3):
    changes.append(('nsemilepmuonsX%i'%i, '', 'min_nsemilepmuons = %i'%i))

for i in xrange(0,3):
    changes.append(('nleptonsX%i'%i, '', 'min_nleptons = %i'%i))

for i in xrange(0,3):
    changes.append(('nsemileptonsX%i'%i, '', 'min_nsemileptons = %i'%i))

for i in xrange(0,25):
    changes.append(('ntracks01X%i'%i, '', 'min_ntracks01 = %i'%i))

for i in xrange(0,101,5):
    changes.append(('maxtrackpt01X%i'%i, '', 'min_maxtrackpt01 = %i'%i))

for i in xrange(0,10):
    changes.append(('njetsntks01X%i'%i, '', 'min_njetsntks01 = %i'%i))

for i in xrange(0,200,10):
    changes.append(('tkonlymass01X%i'%i, '', 'min_tkonlymass01 = %i'%i))

for i in xrange(0,501,25):
    changes.append(('jetsntkmass01X%i'%i, '', 'min_jetsntkmass01 = %i'%i))

for i in xrange(0,501,25):
    changes.append(('tksjetsntkmass01X%i'%i, '', 'min_tksjetsntkmass01 = %i'%i))

for i in xrange(0,32,2):
    changes.append(('absdeltaphi01X%s'%pize(0.1*i,1), '', 'min_absdeltaphi01 = %f'%(0.1*i)))

for i in xrange(0,100):
    changes.append(('svdist2dX%s'%pize(0.0025*i,4), '', 'min_svdist2d = %f'%(0.0025*i)))

for name, vtx_change, ana_change in changes:
    vtx_name = 'Sel' + name
    ana_name = 'Ana' + name
    path_name = name

    vtx_obj = eval('vtx_sel.clone(%s)' % vtx_change)
    ana_obj = eval('ana_sel.clone(%s)' % ana_change)

    ana_obj.vertex_src = vtx_name
    
    setattr(process, vtx_name, vtx_obj)
    setattr(process, ana_name, ana_obj)

    setattr(process, path_name, cms.Path(vtx_obj * ana_obj))


if use_weights:
    process.load('JMTucker.MFVNeutralino.WeightProducer_cfi')

import JMTucker.Tools.SimpleTriggerEfficiency_cfi as SimpleTriggerEfficiency
SimpleTriggerEfficiency.setup_endpath(process, weight_src='mfvWeight' if use_weights else '')


if __name__ == '__main__' and hasattr(sys, 'argv') and 'submit' in sys.argv:
    import JMTucker.Tools.Samples as Samples
    samples = Samples.from_argv([Samples.mfv_neutralino_tau0100um_M0400,
                                 Samples.mfv_neutralino_tau1000um_M0400,
                                 Samples.mfv_neutralino_tau0300um_M0400,
                                 Samples.mfv_neutralino_tau9900um_M0400] + Samples.ttbar_samples + Samples.qcd_samples)

    from JMTucker.Tools.CRABSubmitter import CRABSubmitter
    cs = CRABSubmitter('CutPlayV19',
                       job_control_from_sample = True,
                       use_ana_dataset = True,
                       run_half_mc = True,
                       )
    cs.submit_all(samples)

