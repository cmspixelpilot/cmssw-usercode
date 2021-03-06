import FWCore.ParameterSet.Config as cms


JECPATProducer = cms.EDProducer('JECPATProducer',
                                jet_src =cms.InputTag('selectedPatJetsPF'),
                                use_correction = cms.bool(True), # Use correction at all
                                jes_uncertainty = cms.bool(True), # True for JES and False for JER
                                jes_way = cms.bool(True), # True = up, False = down
                                jer_way = cms.bool(True) ) # True = up, False = down
