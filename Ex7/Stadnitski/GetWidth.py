#/usr/bin/env python
from array import array
import numpy as np
from ROOT import *

def main():

    HDECAY = write(np.loadtxt('HDECAY/br.sm2', skiprows = 2))
    read(HDECAY)

    print('Reached end of main.')
    
def write(data):

    fileName = 'sim.root'
    sim = TFile.Open(fileName, 'RECREATE')

    m = array('f', [0])
    massTree = TTree('massTree', 'Higgs mass variable')
    massTree.Branch('m', m, 'm/F')

    w = array('f', [0])
    widthTree = TTree('widthTree', 'Decay width variable')
    widthTree.Branch('w', w, 'w/F')

    for d in data:

        m[0] = d[0]
        massTree.Fill()

        w[0] = d[-1]
        widthTree.Fill()

    massTree.Write()
    widthTree.Write()
    sim.Close()

    return fileName

def read(fileName):

    canvas = TCanvas('Canvas', '', 600, 600)
    canvas.SetMargin(0.2, 0.1, 0.1, 0.1)
    canvas.cd()
    
    sim = TFile.Open(fileName, 'READ')
    massTree = sim.Get('massTree')
    widthTree = sim.Get('widthTree')

    m, w = array( 'f' ), array( 'f' )
    massLeaf = massTree.GetLeaf('m')
    widthLeaf = widthTree.GetLeaf('w')

    N = massTree.GetEntries()

    for i in range(N):
        massTree.GetEntry(i)
        m.append(massLeaf.GetValue())
        widthTree.GetEntry(i)
        w.append(widthLeaf.GetValue())

    graph = TGraph(N, m, w)
    graph.Draw('A*')

    graph.SetTitle('HDECAY mass-width plot')
    graph.GetXaxis().SetTitle('Higgs mass')
    graph.GetXaxis().CenterTitle(True)
    graph.GetYaxis().SetTitle('Decay width')
    graph.GetYaxis().CenterTitle(True)

    canvas.Print('graph.png')

if __name__ == '__main__': main()

'''
    canvas = TCanvas('Canvas', '', 600, 600)
    canvas.SetFillColor(0)
    canvas.cd()
    
    normals = TFile.Open('normals.root', 'READ')
    tree = normals.Get('tree')
    hist = TH1F('hist', 'Standard Gaussian, N = 1000', 100, -4, 4)
    
    n = array('f', [0])
    tree.Branch('n', n, 'n/F')
    N = tree.GetEntries()
        
    for i in tree: hist.Fill(i.n)

    hist.SetFillColor(5)
    hist.SetLineColor(1)
    hist.SetLineWidth(3)

    hist.GetXaxis().SetTitle('Simulated variable')
    hist.GetXaxis().CenterTitle(True)
    hist.GetYaxis().SetTitle('Number of hits')
    hist.GetYaxis().CenterTitle(True)

    hist.Fit('gaus')
    hist.SetStats(0)
    hist.Draw()

    canvas.Print('graph.C')
    canvas.Print('graph.eps')
    canvas.Print('graph.png')
    
    print('Reached end of main')

'''