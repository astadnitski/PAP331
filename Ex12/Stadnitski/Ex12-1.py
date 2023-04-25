#!/usr/bin/env python

import hist
import multiprocessing
import uproot

from coffea import processor

class Analysis(processor.ProcessorABC):

    def __init__(self):
        self.histograms = {}
        self.histograms['pileup'] = (
            hist.Hist.new
            .Reg(60, 0, 60, name = 'x', label = 'Number of primary vertices')
            .Double())

    def process(self, events):
        out = {}
        self.histograms['pileup'].fill(x = events[events.HLT_IsoMu24 == True].PV_npvs)
        out.update(self.histograms)
        return out

    def postprocess(self, accumulator): pass

def main():
    
    sample = {'DYJetsToLL': ['DYJetsToLL.root']}

    job_executor = processor.FuturesExecutor(workers = max(multiprocessing.cpu_count() - 1, 1))
    
    run = processor.Runner(
        executor = job_executor,
        chunksize = 1000000,
        maxchunks = None)

    result = run(sample, 'Events', Analysis())

    with uproot.recreate('output1.root') as output:
        for key in result.keys(): output[f'{key}'] = result[key]

if __name__ == '__main__': main()