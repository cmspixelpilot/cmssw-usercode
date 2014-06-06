import FWCore.ParameterSet.Config as cms

mfvSelectedVertices = cms.EDProducer('MFVVertexSelector',
                                     vertex_src = cms.InputTag('mfvVertices'),
                                     vertex_aux_src = cms.InputTag('mfvVerticesAux'),
                                     produce_vertices = cms.bool(False),
                                     produce_tracks = cms.bool(False),
                                     produce_refs = cms.bool(False),
                                     use_mva = cms.bool(False),
                                     mva_cut = cms.double(0.7),
                                     min_ntracks          = cms.int32(0),
                                     max_ntracks          = cms.int32(1000000),
                                     min_ntracksptgt3     = cms.int32(0),
                                     min_ntracksptgt5     = cms.int32(0),
                                     min_ntracksptgt10    = cms.int32(0),
                                     min_njetsntks        = cms.int32(0),
                                     max_njetsntks        = cms.int32(1000000),
                                     max_chi2dof          = cms.double(1e9),
                                     min_tkonlypt         = cms.double(0),
                                     max_abstkonlyeta     = cms.double(1e9),
                                     min_tkonlymass       = cms.double(0),
                                     min_jetsntkpt        = cms.double(0),
                                     max_absjetsntketa    = cms.double(1e9),
                                     min_jetsntkmass      = cms.double(0),
                                     min_tksjetsntkpt     = cms.double(0),
                                     max_abstksjetsntketa = cms.double(1e9),
                                     min_tksjetsntkmass   = cms.double(0),
                                     min_costhtkonlymombs = cms.double(-3),
                                     min_costhjetsntkmombs = cms.double(-3),
                                     min_costhtksjetsntkmombs = cms.double(-3),
                                     min_missdisttkonlypvsig = cms.double(0),
                                     min_missdistjetsntkpvsig = cms.double(0),
                                     min_missdisttksjetsntkpvsig = cms.double(0),
                                     min_sumpt2           = cms.double(0),
                                     min_maxtrackpt       = cms.double(0),
                                     min_maxm1trackpt     = cms.double(0),
                                     min_maxm2trackpt     = cms.double(0),
                                     max_trackdxyerrmin   = cms.double(1e9),
                                     max_trackdxyerrmax   = cms.double(1e9),
                                     max_trackdxyerravg   = cms.double(1e9),
                                     max_trackdxyerrrms   = cms.double(1e9),
                                     max_trackdzerrmin    = cms.double(1e9),
                                     max_trackdzerrmax    = cms.double(1e9),
                                     max_trackdzerravg    = cms.double(1e9),
                                     max_trackdzerrrms    = cms.double(1e9),
                                     min_drmin            = cms.double(0),
                                     max_drmin            = cms.double(1e9),
                                     min_drmax            = cms.double(0),
                                     max_drmax            = cms.double(1e9),
                                     max_jetpairdrmin     = cms.double(1e9),
                                     max_jetpairdrmax     = cms.double(1e9),
                                     max_err2d            = cms.double(1e9),
                                     max_err3d            = cms.double(1e9),
                                     min_gen3dsig         = cms.double(0),
                                     max_gen3dsig         = cms.double(1e6),
                                     min_bs2ddist         = cms.double(0),
                                     max_bs2ddist         = cms.double(1e9),
                                     min_bs2derr          = cms.double(0),
                                     max_bs2derr          = cms.double(1e9),
                                     min_bs2dsig          = cms.double(0),
                                     min_bs3ddist         = cms.double(0),
                                     max_sumnhitsbehind   = cms.int32(1000000),
                                     bs_hemisphere        = cms.int32(0),
                                     max_ntrackssharedwpv = cms.int32(1000000),
                                     max_ntrackssharedwpvs = cms.int32(1000000),
                                     max_npvswtracksshared = cms.int32(1000000),
                                     sort_by = cms.string('ntracks_then_mass'),
                                     )

mfvSelectedVerticesLoose = mfvSelectedVertices.clone(
    min_ntracks = 5
    )

mfvSelectedVerticesMedium = mfvSelectedVertices.clone(
    min_ntracks = 5,
    max_drmin = 0.4,
    max_drmax = 4,
    max_bs2ddist = 2.87,
    max_bs2derr = 0.004,
    min_ntracksptgt3 = 3,
    max_sumnhitsbehind = 0,
    )

mfvSelectedVerticesTight = mfvSelectedVertices.clone(
    min_ntracks = 5,
    max_drmin = 0.4,
    min_drmax = 1.2,
    max_drmax = 4,
    max_bs2ddist = 2.87,
    max_bs2derr = 0.0025,
    min_njetsntks = 1,
    min_ntracksptgt3 = 3,
    max_sumnhitsbehind = 0,
    )

mfvSelectedVerticesTightSig = mfvSelectedVerticesTight.clone(
    min_ntracks = 7
    )

mfvSelectedVerticesTightLargeErr = mfvSelectedVerticesTight.clone(
    min_bs2derr = 0.008,
    max_bs2derr = 1e9,
    )

mfvSelectedVerticesSeq = cms.Sequence(mfvSelectedVerticesLoose * mfvSelectedVerticesTight * mfvSelectedVerticesTightSig * mfvSelectedVerticesMedium * mfvSelectedVerticesTightLargeErr)
