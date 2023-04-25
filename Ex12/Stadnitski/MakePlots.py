#!/usr/bin/env python

import ROOT

def read(part, method):

    canvas = ROOT.TCanvas('Canvas', '', 600, 600)
    canvas.SetFillColor(0)
    canvas.cd()
    
    pileup = ROOT.TFile.Open('output' + str(part) + '.root', 'READ')
    hist = pileup.Get('pileup')

    hist.GetXaxis().SetTitle('Number of primary vertices')
    hist.GetXaxis().CenterTitle(True)
    hist.GetYaxis().SetTitle('Number of hits')
    hist.GetYaxis().CenterTitle(True)

    hist.SetTitle('Pileup distribution [' + method + ']')
    hist.SetFillColor(part * 2)
    hist.SetStats(0)
    hist.Draw()

    canvas.Print('Plots/plot' + str(part) + '.pdf')
    canvas.Print('Plots/plot' + str(part) + '.png')
    canvas.Print('Plots/plot' + str(part) + '.eps')

def main():
    read(1, 'Coffea')
    read(2, 'RDataFrame')

if __name__ == '__main__': main()