from JMTucker.Tools.CMSSWTools import set_events_to_process

rle_fns = {
    'ttbarhadronic': (
        [(1, 270628, 81171953), (1, 138459, 41529292), (1, 63100, 18926244), (1, 86777, 26027784), (1, 337645, 101273223), (1, 37830, 11346593), (1, 180593, 54166923), (1, 34727, 10416034), (1, 323384, 96995659), (1, 193695, 58096779), (1, 277640, 83275191), (1, 303872, 91143141), (1, 28644, 8591209), (1, 285795, 85721324), (1, 61727, 18514396), (1, 45410, 13620094), (1, 24101, 7228845), (1, 27608, 8280532), (1, 170081, 51013910), (1, 314208, 94243469), (1, 295065, 88501532)],
        '''/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/0E9DCF01-0216-E211-934F-20CF3019DF0F.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/36C26A30-4016-E211-8C50-00259073E4A2.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/9A4CAE1D-1216-E211-9A5B-001EC9D7F67B.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/72E91B87-4D16-E211-910A-001EC9D29E23.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/B877A779-1E16-E211-86CC-00259073E3FE.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/FE803252-1616-E211-A96C-E0CB4E19F9B5.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/0C3B53A1-2416-E211-BAE6-00259073E474.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/F61274AB-3C16-E211-8DCD-E0CB4E1A118D.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/42E0BB91-2216-E211-B5D8-20CF3027A627.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/887B6352-4716-E211-B480-485B39800B86.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/38B535BC-2616-E211-9018-001EC9D825CD.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/80565691-2E16-E211-ADA2-001EC9D8B15D.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/28ACB890-BB15-E211-870E-00259073E536.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/CC9F7FCD-B115-E211-9719-00259073E30E.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/00827D8A-D615-E211-BDB9-485B39800C15.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/F22200FF-8315-E211-BA7C-E0CB4E29C517.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/1C8B60C0-0116-E211-937D-00259073E42E.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/CAC9D7E3-1516-E211-A69F-E0CB4EA0A939.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/685BCDDC-4216-E211-B132-00259073E524.root
/store/mc/Summer12_DR53X/TTJets_HadronicMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A-v1/00000/0E77F79F-DA15-E211-A2D3-E0CB4E1A1163.root'''.split('\n')
        ),
    'ttbarsemilep': (
        [(1, 164679, 49393874), (1, 38170, 11448684), (1, 104193, 31251665), (1, 109235, 32763967), (1, 260177, 78037433), (1, 305325, 91578980), (1, 204297, 61276740), (1, 214031, 64196227), (1, 252746, 75808475), (1, 79046, 23708891), (1, 139892, 41959244), (1, 31143, 9341047), (1, 3685, 1105017), (1, 30020, 9004000), (1, 245748, 73709629), (1, 228678, 68589419), (1, 80994, 24293268), (1, 284501, 85333022)],
        '''/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/F8F3920D-6B24-E211-84D2-002590200B78.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00002/DA8F6382-8726-E211-898E-001E67397CBA.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00002/22443C35-4626-E211-8F70-001E67398B29.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/96E4B66F-9C24-E211-B340-003048D46300.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00001/286E0737-C225-E211-97E9-001E6739834A.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00002/F82401F8-DA25-E211-92E5-001E6739753A.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00002/C4135982-E825-E211-ADEF-002590200918.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00002/5A9CCD86-1426-E211-918E-001E67397EDB.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/0435FBE6-5424-E211-9DD8-00304866C51E.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/487F159C-0B24-E211-AD57-0025B3E063A6.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/863CEB83-0C24-E211-A693-002590200B00.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/C00F10C5-0C24-E211-A8B8-001E6739825A.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/2213CC18-0B24-E211-A818-003048673EFE.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00002/A2D100B8-5A26-E211-A886-00259020080C.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/0C17FAF7-9B24-E211-9873-003048D47730.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00001/76DBA269-C025-E211-9CE3-0025B3E05BA8.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00001/6C1E6C1D-B525-E211-B03C-002590200A98.root
/store/mc/Summer12_DR53X/TTJets_SemiLeptMGDecays_8TeV-madgraph/AODSIM/PU_S10_START53_V7A_ext-v1/00000/0E16A7C1-0B24-E211-AB06-001E6739732D.root'''.split('\n')
        ),
    'qcdht0500': (
        [(1, 276978, 83076688), (1, 42147, 12641318), (1, 264525, 79341612)],
        '''/store/mc/Summer12_DR53X/QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00002/92371F42-0924-E211-BFC2-00266CFAE484.root
/store/mc/Summer12_DR53X/QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/14A95E6D-551F-E211-A47D-00266CFAE6A4.root
/store/mc/Summer12_DR53X/QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00002/C40792F3-0722-E211-8C9F-848F69FD28AA.root'''.split('\n')
        ),
    'qcdht1000': (
        [(1, 133401, 40012176),(1, 137948, 41376070), (1, 56799, 17036136), (1, 108471, 32534642), (1, 130433, 39121853), (1, 57486, 17242161), (1, 101083, 30318687), (1, 54590, 16373540), (1, 75217, 22560365), (1, 162294, 48678310), (1, 26515, 7952956), (1, 142647, 42785337), (1, 77848, 23349761), (1, 12351, 3704431), (1, 24654, 7394794)],
        '''/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/E4C45BB8-DC0E-E211-93C6-008CFA001DB8.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/563252B0-A50E-E211-9FF6-848F69FD4ED1.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/E8627EF8-9B0E-E211-96B5-0024E876A82E.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/A2CEDDF1-870D-E211-A98D-00266CF258D8.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/6620B2CC-AF0C-E211-BB0C-008CFA007F18.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00001/726D8C91-050F-E211-8A88-00266CF271E8.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/CCD1039F-6D0E-E211-97ED-008CFA000F5C.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/44DFF43E-7F0E-E211-BFC5-00266CFAE78C.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/EC8576B7-270E-E211-AD08-848F69FD4565.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/0264810B-570E-E211-9B1B-0026B94E2872.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/48C264E5-3B0E-E211-A077-0024E8769AF8.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/FE0ABBDC-CB0E-E211-87C9-00266CFAE518.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/D6CAC24F-840C-E211-A2E1-00266CFAE7AC.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/A2B6956F-7A0C-E211-939D-00266CF9AFF0.root
/store/mc/Summer12_DR53X/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/AODSIM/PU_S10_START53_V7A-v1/00000/5C56ADB0-EE0D-E211-8001-848F69FD2919.root'''.split('\n')
        ),
    }

def setup(process, sample):
    rle, fns = rle_fns[sample]
    set_events_to_process(process, rle)
    process.source.fileNames = fns
