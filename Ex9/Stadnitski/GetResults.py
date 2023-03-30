#/usr/bin/env python
from array import array
import numpy as np
import re
from ROOT import *

def plot(variable, lower, upper):

    canvas = TCanvas('Canvas', '', 600, 600)
    canvas.SetFillColor(0)
    canvas.cd()
    
    results = TFile.Open('results.root', 'READ')
    hist = TH1F('hist', variable + ' distribution, N = 1000', 100, np.floor(lower), np.ceil(upper))

    if variable == 'Transverse-momentum':
        tree = results.Get('treeT')
        t = array('f', [0])
        tree.Branch('t', t, 't/F') 
        for i in tree: hist.Fill(i.t)
    elif variable == 'Pseudorapidity':
        tree = results.Get('treeP')
        p = array('f', [0])
        tree.Branch('p', p, 'p/F') 
        for i in tree: hist.Fill(i.p)

    hist.GetXaxis().SetTitle(variable)
    hist.GetXaxis().CenterTitle(True)
    hist.GetYaxis().SetTitle('Number of events')
    hist.GetYaxis().CenterTitle(True)

    if variable == 'Transverse-momentum': hist.SetFillColor(7)
    elif variable == 'Pseudorapidity': hist.SetFillColor(6)

    hist.SetLineColor(1)
    hist.SetStats(0)
    hist.Draw()

    plotName = 'plots/' + variable + '-histogram'
    canvas.Print(plotName + '.C')
    canvas.Print(plotName + '.eps')
    canvas.Print(plotName + '.png')
    print('Saved plots to subdirectory')

def part1():

    ### WRITE ###

    transverse, pseudo = [], []
    keyT = re.compile('Transverse momentum : \d*\.\d*')
    keyP = re.compile('Pseudorapidity : -*\d*\.\d*')

    for row, line in enumerate(open('output.txt')):

        for match in re.finditer(keyT, line):
            select = match.group().split(' ')
            transverse.append(float(select[-1]))

        for match in re.finditer(keyP, line):
            select = match.group().split(' ')
            pseudo.append(float(select[-1]))
    
    results = TFile.Open('results.root', 'RECREATE')
    treeT = TTree('treeT', 'Tree of transverse momenta')
    treeP = TTree('treeP', 'Tree of pseudorapidities')

    t = array('f', [0])
    treeT.Branch('t', t, 't/F')
    for i in transverse:
        t[0] = i
        treeT.Fill()
    treeT.Write()
    
    p = array('f', [0])
    treeP.Branch('p', p, 'p/F')
    for i in pseudo:
        p[0] = i
        treeP.Fill()
    treeP.Write()

    results.Close()
    print('Saved results to ROOT file')

    ### READ ###

    plot('Transverse-momentum', min(transverse), max(transverse))
    plot('Pseudorapidity', min(pseudo), max(pseudo))

    return transverse, pseudo

def part2(transverse, pseudo):

    selected, total = 0.0, len(transverse)
    for i in range(total):
        if transverse[i] > 5 and np.abs(pseudo[i]) < 2.5: selected += 1

    return selected / total

def main():  
    transverse, pseudo = part1()
    probability = part2(transverse, pseudo)
    print('Part 1 : plots saved in ./plots')
    print('Part 2 : probability of event selection is ' + str(probability))
    
if __name__ == '__main__': main()