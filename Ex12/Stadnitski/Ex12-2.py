#!/usr/bin/env python

import ROOT

ROOT.ROOT.EnableImplicitMT()

def main():

    data = ROOT.RDataFrame('Events', 'DYJetsToLL.root')
    data = data.Filter('HLT_IsoMu24 == true', 'Events passing the selected trigger')

    selectedData = data.Define('Selected', 'PV_npvs')
    hist = selectedData.Histo1D(('pileup', 'Pileup distribution (RDataFrame); Number of primary vertices; Number of hits', 60, 0, 60), 'PV_npvs')
    
    output = ROOT.TFile.Open('output2.root', 'RECREATE')
    hist.Write()
    output.Close()

if __name__ == '__main__': main()