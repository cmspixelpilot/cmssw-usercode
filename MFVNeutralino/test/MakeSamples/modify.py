import FWCore.ParameterSet.Config as cms

def set_particle_tau0(process, id, tau0):
    params = [x for x in process.generator.PythiaParameters.processParameters.value() if ':tau0' not in x]
    process.generator.PythiaParameters.processParameters = params
    process.generator.PythiaParameters.processParameters.append('%i:tau0 = %f' % (id, tau0)) # tau0 is in mm by pythia convention

def set_tune(process, tune):
    params = [x for x in process.generator.PythiaParameters.processParameters.value() if 'Tune' not in x]
    process.generator.PythiaParameters.processParameters = params
    process.generator.PythiaParameters.processParameters.append('Tune:pp %i' % tune)
    
def set_gluino_tau0(process, tau0):
    set_particle_tau0(process, 1000021, tau0)

def set_neutralino_tau0(process, tau0):
    set_particle_tau0(process, 1000022, tau0)

def set_mass(m_gluino, fn='minSLHA.spc'):
    slha = '''
BLOCK SPINFO  # Spectrum calculator information
     1   Minimal    # spectrum calculator
     2   1.0.0         # version number
#
BLOCK MODSEL  # Model selection
     1     1   #
#

BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
  1000021     %(m_gluino)E       # ~g

DECAY   1000021     0.01E+00   # gluino decays
#           BR         NDA      ID1       ID2       ID3
     0.5E+00          3            3          5           6   # BR(~g -> s b t)
     0.5E+00          3           -3         -5          -6   # BR(~g -> sbar bbar tbar)
'''
    open(fn, 'wt').write(slha % locals())

def set_masses(m_gluino, m_neutralino, fn='minSLHA.spc'):
    slha = '''
BLOCK SPINFO  # Spectrum calculator information
     1   Minimal    # spectrum calculator
     2   1.0.0         # version number
#
BLOCK MODSEL  # Model selection
     1     1   #
#

BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
  1000021     %(m_gluino)E       # ~g
  1000022     %(m_neutralino)E   # ~chi_10

DECAY   1000021     0.01E+00   # gluino decays
#          BR         NDA      ID1       ID2
    1.0E00            2      1000022    21   # BR(~g -> ~chi_10  g)

DECAY   1000022     0.01E+00   # neutralino decays
#           BR         NDA      ID1       ID2       ID3
     0.5E+00          3            3          5           6   # BR(~chi_10 -> s b t)
     0.5E+00          3           -3         -5          -6   # BR(~chi_10 -> sbar bbar tbar)
'''
    open(fn, 'wt').write(slha % locals())


def prefer_it(process, name, connect, record, tag):
    from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
    es_source = cms.ESSource('PoolDBESSource', CondDBSetup, connect = cms.string(connect), toGet = cms.VPSet(cms.PSet(record = cms.string(record), tag = cms.string(tag))))
    es_prefer = cms.ESPrefer('PoolDBESSource', name)
    setattr(process, name, es_source)
    setattr(process, 'es_prefer_' + name, es_prefer)

def ideal_bs_tag(process):
    prefer_it(process, 'idealCenteredBS', 'frontier://FrontierProd/CMS_COND_31X_BEAMSPOT', 'BeamSpotObjectsRcd', 'Ideal_Centered_MC_44_V1')

def gauss_bs(process, noxy=False, noz=False):
    ideal_bs_tag(process)
    from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import VtxSmearedCommon, GaussVtxSmearingParameters
    process.VtxSmeared = cms.EDProducer("GaussEvtVtxGenerator", GaussVtxSmearingParameters, VtxSmearedCommon)
    if noxy:
        process.VtxSmeared.SigmaX = 1e-12
        process.VtxSmeared.SigmaY = 1e-12
    if noz:
        process.VtxSmeared.SigmaZ = 1e-12

def center_bs(process):
    ideal_bs_tag(process)
    process.VtxSmeared.X0 = 0
    process.VtxSmeared.Y0 = 0
    process.VtxSmeared.Y0 = 0

def nopu(process):
    process.load('SimGeneral.MixingModule.mixNoPU_cfi')

def ttbar(process):
    process.generator.PythiaParameters.processParameters = cms.vstring(
        'Main:timesAllowErrors = 10000',
        'Top:gg2ttbar = on',
        'Top:qqbar2ttbar = on',
        '24:onMode = off',
        '24:onIfAny = 1 2 3 4 5',
        'Tune:pp 5',
        )

def tracker_alignment(process, tag):
    prefer_it(process, 'tkAlign', 'frontier://FrontierPrep/CMS_COND_ALIGNMENT', 'TrackerAlignmentRcd', 'TrackerAlignment_2010RealisticPlus%s_mc' % tag.capitalize())

def keep_random_info(process):
    process.output.outputCommands += [
        'drop *_randomEngineStateProducer_*_*',
        'drop CrossingFramePlaybackInfoExtended_*_*_*'
        ]

def castor_thing(process):
    prefer_it(process, 'castorThing', 'frontier://FrontierProd/CMS_COND_HCAL_000', 'CastorSaturationCorrsRcd', 'CastorSaturationCorrs_v1.00_mc')

def keep_tracker_extras(process):
    process.output.outputCommands += [
        'keep recoTrackExtras_generalTracks__*',
        'keep TrackingRecHitsOwned_generalTracks__*'
        ]

class DummyBeamSpots():
    myttbarBowing = cms.PSet(
            X0 = cms.double(0.246344),
            Y0 = cms.double(0.389749),
            Z0 = cms.double(0.402745),
            SigmaZ = cms.double(5.98845),
            dxdz = cms.double(1.70494e-05),
            dydz = cms.double(-2.13481e-06),
            BeamWidthX = cms.double(0.00151667),
            BeamWidthY = cms.double(0.00151464),
            covariance = cms.vdouble(1.24561e-10, 5.32196e-13, 0, 0, 0, 0, 0, 1.24935e-10, 0, 0, 0, 0, 0, 0.00445375, 0, 0, 0, 0, 0.00222686, 0, 0, 0, 3.36155e-12, 2.7567e-14, 0, 3.37374e-12, 0, 2.97592e-10),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )

    myttbarCurl = cms.PSet(
            X0 = cms.double(0.246597),
            Y0 = cms.double(0.38699),
            Z0 = cms.double(0.314451),
            SigmaZ = cms.double(5.99379),
            dxdz = cms.double(-1.9081e-06),
            dydz = cms.double(-1.02914e-05),
            BeamWidthX = cms.double(0.00147516),
            BeamWidthY = cms.double(0.00150106),
            covariance = cms.vdouble(1.23255e-10, 5.60119e-13, 0, 0, 0, 0, 0, 1.22964e-10, 0, 0, 0, 0, 0, 0.0045269, 0, 0, 0, 0, 0.00226344, 0, 0, 0, 3.30386e-12, 2.14557e-14, 0, 3.3566e-12, 0, 2.93467e-10),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )

    myttbarElliptical = cms.PSet(
            X0 = cms.double(0.246156),
            Y0 = cms.double(0.389613),
            Z0 = cms.double(0.288198),
            SigmaZ = cms.double(5.97317),
            dxdz = cms.double(5.21863e-06),
            dydz = cms.double(7.79036e-06),
            BeamWidthX = cms.double(0.00149346),
            BeamWidthY = cms.double(0.00148959),
            covariance = cms.vdouble(1.23521e-10, 8.78629e-13, 0, 0, 0, 0, 0, 1.22967e-10, 0, 0, 0, 0, 0, 0.00439882, 0, 0, 0, 0, 0.0021994, 0, 0, 0, 3.33981e-12, 3.81918e-14, 0, 3.32571e-12, 0, 2.91985e-10),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )

    myttbarRadial = cms.PSet(
            X0 = cms.double(0.246322),
            Y0 = cms.double(0.389811),
            Z0 = cms.double(0.327943),
            SigmaZ = cms.double(6.08119),
            dxdz = cms.double(6.83738e-06),
            dydz = cms.double(1.8884e-07),
            BeamWidthX = cms.double(0.00149758),
            BeamWidthY = cms.double(0.00153033),
            covariance = cms.vdouble(1.22914e-10, 5.21468e-13, 0, 0, 0, 0, 0, 1.24135e-10, 0, 0, 0, 0, 0, 0.00459276, 0, 0, 0, 0, 0.00229637, 0, 0, 0, 3.28346e-12, 1.84415e-14, 0, 3.32401e-12, 0, 2.91313e-10),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )

    myttbarSagitta = cms.PSet(
            X0 = cms.double(0.235756),
            Y0 = cms.double(0.389839),
            Z0 = cms.double(0.451828),
            SigmaZ = cms.double(5.9656),
            dxdz = cms.double(-6.12007e-06),
            dydz = cms.double(-3.34286e-06),
            BeamWidthX = cms.double(0.00142781),
            BeamWidthY = cms.double(0.00146079),
            covariance = cms.vdouble(1.21587e-10, 1.2445e-12, 0, 0, 0, 0, 0, 1.22063e-10, 0, 0, 0, 0, 0, 0.00443525, 0, 0, 0, 0, 0.00221762, 0, 0, 0, 3.24618e-12, 2.20384e-14, 0, 3.29028e-12, 0, 2.87833e-10),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )

    myttbarSkew = cms.PSet(
            X0 = cms.double(0.246258),
            Y0 = cms.double(0.389962),
            Z0 = cms.double(0.386416),
            SigmaZ = cms.double(6.02712),
            dxdz = cms.double(-0.00011416),
            dydz = cms.double(-7.07232e-06),
            BeamWidthX = cms.double(0.00164608),
            BeamWidthY = cms.double(0.00151397),
            covariance = cms.vdouble(1.26645e-10, 7.7728e-14, 0, 0, 0, 0, 0, 1.25663e-10, 0, 0, 0, 0, 0, 0.00445011, 0, 0, 0, 0, 0.00222484, 0, 0, 0, 3.39247e-12, 1.9986e-14, 0, 3.34669e-12, 0, 3.14378e-10),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )

    myttbarTelescope = cms.PSet(
            X0 = cms.double(0.245667),
            Y0 = cms.double(0.386495),
            Z0 = cms.double(0.425672),
            SigmaZ = cms.double(6.16219),
            dxdz = cms.double(3.75215e-06),
            dydz = cms.double(-1.91476e-06),
            BeamWidthX = cms.double(0),
            BeamWidthY = cms.double(0),
            covariance = cms.vdouble(3.44758e-10, 3.61193e-13, 0, 0, 0, 0, 0, 3.46413e-10, 0, 0, 0, 0, 0, 0.000100795, 0, 0, 0, 0, 9.63705e-05, 0, 0, 0, 9.41413e-12, 7.89166e-14, 0, 9.46686e-12, 0, 0),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )

    myttbarTwist = cms.PSet(
            X0 = cms.double(0.246196),
            Y0 = cms.double(0.389666),
            Z0 = cms.double(0.293139),
            SigmaZ = cms.double(6.0066),
            dxdz = cms.double(4.09512e-06),
            dydz = cms.double(1.19775e-05),
            BeamWidthX = cms.double(0.00148173),
            BeamWidthY = cms.double(0.00149055),
            covariance = cms.vdouble(1.22449e-10, 0, 0, 0, 0, 0, 0, 1.22109e-10, 0, 0, 0, 0, 0, 0.0045879, 0, 0, 0, 0, 0.00229394, 0, 0, 0, 3.27196e-12, 7.22971e-15, 0, 3.27492e-12, 0, 2.89948e-10),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )

    myttbarZexpansion = cms.PSet(
            X0 = cms.double(0.246214),
            Y0 = cms.double(0.389698),
            Z0 = cms.double(0.394112),
            SigmaZ = cms.double(6.00186),
            dxdz = cms.double(3.61695e-06),
            dydz = cms.double(1.45456e-06),
            BeamWidthX = cms.double(0.0014962),
            BeamWidthY = cms.double(0.00149599),
            covariance = cms.vdouble(1.24303e-10, 7.70197e-13, 0, 0, 0, 0, 0, 1.22716e-10, 0, 0, 0, 0, 0, 0.00449324, 0, 0, 0, 0, 0.00224661, 0, 0, 0, 3.3007e-12, 2.37285e-14, 0, 3.20966e-12, 0, 2.94185e-10),
            EmittanceX = cms.double(0),
            EmittanceY = cms.double(0),
            BetaStar = cms.double(0),
        )
    
def dummy_beamspot(process, params):
    params = getattr(DummyBeamSpots, params)

    process.myBeamSpot = cms.EDProducer('DummyBeamSpotProducer', params)

    for name, path in process.paths.items():
        path.insert(0, process.myBeamSpot)

    for name, out in process.outputModules.items():
        new_cmds = []
        for cmd in out.outputCommands:
            if 'offlineBeamSpot' in cmd:
                new_cmds.append(cmd.replace('offlineBeamSpot', 'myBeamSpot'))
        out.outputCommands += new_cmds

    import itertools
    from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag
    for path_name, path in itertools.chain(process.paths.iteritems(), process.endpaths.iteritems()):
        massSearchReplaceAnyInputTag(path, cms.InputTag('offlineBeamSpot'), cms.InputTag('myBeamSpot'), verbose=True)

def hlt_filter(process, hlt_path):
    from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
    process.triggerFilter = hltHighLevel.clone()
    process.triggerFilter.HLTPaths = [hlt_path]
    process.triggerFilter.andOr = True # = OR
    process_out = None
    try:
        process_out = process.output
    except AttributeError:
        process_out = process.out
    if hasattr(process_out, 'SelectEvents'):
        raise ValueError('process_out already has SelectEvents: %r' % process_out.SelectEvents)
    process_out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('ptriggerFilter'))
    for name, path in process.paths.items():
        path.insert(0, process.triggerFilter)
    process.ptriggerFilter = cms.Path(process.triggerFilter)
    if hasattr(process, 'schedule'):
        process.schedule.insert(0, process.ptriggerFilter)
