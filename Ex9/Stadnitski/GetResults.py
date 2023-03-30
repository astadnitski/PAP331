#/usr/bin/env python
from array import array
import numpy as np
import re
from ROOT import *

def part1():

    transverse, pseudo = [], []
    keyT = re.compile('Transverse momentum : \d*\.\d*')
    keyP = re.compile('Pseudorapidity : \d*\.\d*')

    for row, line in enumerate(open('test.txt')):

        for match in re.finditer(keyT, line):
            select = match.group().split(' ')
            transverse.append(float(select[-1]))

        for match in re.finditer(keyP, line):
            select = match.group().split(' ')
            pseudo.append(float(select[-1]))
    
    results = TFile.Open('results.root', 'RECREATE')
    treeT = TTree('treeT', 'Tree of transverse momenta')

    n = array('f', [0])
    treeT.Branch('n', n, 'n/F')
    for i in transverse:
        n[0] = i
        treeT.Fill()

    treeT.Write()
    results.Close()
    print('Saved results to ROOT file')

    canvas = TCanvas('Canvas', '', 600, 600)
    canvas.SetFillColor(0)
    canvas.cd()
    
    results = TFile.Open('results.root', 'READ')
    treeT = results.Get('treeT')
    hist = TH1F('hist', 'Transverse momenta, N = 1000', 100, 0, 1600)
    
    n = array('f', [0])
    treeT.Branch('n', n, 'n/F')
        
    for i in treeT: hist.Fill(i.n)

    #hist.SetFillColor(3)
    #hist.SetLineColor(1)

    #hist.GetXaxis().SetTitle('Higgs mass [GeV]')
    #hist.GetXaxis().CenterTitle(True)
    #hist.GetYaxis().SetTitle('Number of events')
    #hist.GetYaxis().CenterTitle(True)

    hist.SetStats(0)
    hist.Draw()

    plotName = 'plots/TransverseHistogram'
    canvas.Print(plotName + '.C')
    canvas.Print(plotName + '.eps')
    canvas.Print(plotName + '.png')

def main():
    
    part1()
    
if __name__ == '__main__': main()