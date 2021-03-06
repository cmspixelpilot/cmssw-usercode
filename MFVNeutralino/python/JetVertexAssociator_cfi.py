import FWCore.ParameterSet.Config as cms

mfvVerticesToJets = cms.EDProducer('MFVJetVertexAssociator',
                                   jet_src = cms.InputTag('selectedPatJetsPF'),
                                   vertex_src = cms.InputTag('mfvSelectedVerticesTmp'),
                                   input_is_refs = cms.bool(True),
                                   tag_info_name = cms.string('secondaryVertexMaxDR6p0'),
                                   min_vertex_track_weight = cms.double(0.5),
                                   min_tracks_shared = cms.int32(1),
                                   min_track_pt = cms.double(3),
                                   min_hits_shared = cms.int32(1),
                                   max_cos_angle_diff = cms.double(2),
                                   max_miss_dist = cms.double(1e6),
                                   max_miss_sig = cms.double(2),
                                   histos = cms.untracked.bool(False),
                                   verbose = cms.untracked.bool(False),
                                   )
