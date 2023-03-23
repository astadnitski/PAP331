#/usr/bin/env python
from array import array
import numpy as np
import re
from ROOT import *

def part1():
    return 1

def part2():

    ar = []
    key = re.compile('Measured Higgs mass : \d*\.\d*')
    for row, line in enumerate(open('masses.txt')):
        for match in re.finditer(key, line):
            select = match.group().split(' ')
            ar.append(float(select[-1]))
            #print(ar[-1])
    
    masses = TFile.Open('masses.root', 'RECREATE')
    tree = TTree('tree', 'Tree of Higgs masses')

    n = array('f', [0])
    tree.Branch('n', n, 'n/F')
    for i in ar:
        n[0] = i
        tree.Fill()

    tree.Write()
    masses.Close()
    print('Saved masses to ROOT file')

    canvas = TCanvas('Canvas', '', 600, 600)
    canvas.SetFillColor(0)
    canvas.cd()
    
    masses = TFile.Open('masses.root', 'READ')
    tree = masses.Get('tree')
    hist = TH1F('hist', 'Generated Higgs masses, N = 1000', 100, 124.85, 125.15)
    
    n = array('f', [0])
    tree.Branch('n', n, 'n/F')
        
    for i in tree: hist.Fill(i.n)

    hist.SetFillColor(3)
    hist.SetLineColor(1)
    hist.SetLineWidth(2)

    hist.GetXaxis().SetTitle('Higgs mass [GeV]')
    hist.GetXaxis().CenterTitle(True)
    hist.GetYaxis().SetTitle('Number of events')
    hist.GetYaxis().CenterTitle(True)

    hist.SetStats(0)
    hist.Draw()

    plotName = 'plots/HiggsHistogram'
    canvas.Print(plotName + '.C')
    canvas.Print(plotName + '.eps')
    canvas.Print(plotName + '.png')

    width = 2
    return width

def main():
    with open('WidthRESULTS', 'w') as file:
        file.write('Part 1 width: ' + str(part1()))
        file.write('Part 2 width: ' + str(part2()))
    
if __name__ == '__main__': main()