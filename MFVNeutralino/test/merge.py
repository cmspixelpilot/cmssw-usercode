#!/usr/bin/env python

import sys
from JMTucker.Tools.Merge_cfg import cms, process

if __name__ == '__main__' and hasattr(sys, 'argv') and 'submit' in sys.argv:
    from JMTucker.Tools.CRABSubmitter import CRABSubmitter
    import JMTucker.Tools.Samples as Samples
    from JMTucker.Tools.SampleFiles import SampleFiles
    from JMTucker.Tools.PATTuple_cfg import version as tuple_version

    cs = CRABSubmitter('MFVNtuple' + tuple_version.upper() + 'Merged',
                       total_number_of_events = -1,
                       events_per_job = 50000,
                       get_edm_output = True,
                       data_retrieval = 'fnal_eos',
                       max_threads = 3,
                       manual_datasets = SampleFiles['MFVNtupleV14'],
                       )

    samples = [Samples.dyjetstollM50]

    for sample in samples:
        if sample.is_mc:
            sample.total_events = -1

    cs.submit_all(samples)