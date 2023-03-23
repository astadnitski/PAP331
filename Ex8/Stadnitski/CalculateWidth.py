#/usr/bin/env python
from array import array
import numpy as np
import re
from ROOT import *

def part1():

    loc = -1
    id = re.compile(' id ')
    col = re.compile(' [a-zA-Z]+')
    for row, line in enumerate(open('list.txt')):
        for match0 in re.finditer(id, line):
            for match1 in re.finditer(col, line):
                if match1.group() == ' mWidth': break
                loc += 1

    idx = 0
    id = re.compile('h0')
    col = re.compile(' [a-zA-Z0-9]+\.*[a-zA-Z0-9]*')
    for row, line in enumerate(open('list.txt')):
        for match0 in re.finditer(id, line):
            for match1 in re.finditer(col, line):
                if idx == loc: width = match1.group()
                idx += 1

    return width

def part2():

    ar = []
    key = re.compile('Measured Higgs mass : \d*\.\d*')
    for row, line in enumerate(open('masses.txt')):
        for match in re.finditer(key, line):
            select = match.group().split(' ')
            ar.append(float(select[-1]))
    
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

    ctr = 0
    halfmax = hist.GetMaximum() / 2
    for i in range(100):
        if hist.GetBinContent(i) > halfmax: ctr += 1

    return ctr * hist.GetBinWidth(1)

def main():
    filename = 'WidthRESULTS'
    with open(filename, 'w') as file:
        file.write('Part 1 width\n mWidth in Pythia list output corresponding to h0:' + str(part1()) + ' GeV \n')
        file.write('Part 2 width\n Calculated from histogram of masses (1000 events, 100 bins): ' + str(part2()) + ' GeV')
    print('Saved results to ' + filename)
    
if __name__ == '__main__': main()