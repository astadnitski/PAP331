#/usr/bin/env python
from array import array
import numpy as np
from ROOT import *

def main():

    HDECAY = write('HDECAY')
    read(HDECAY)

    FEYNHIGGS = write('FEYNHIGGS')
    read(FEYNHIGGS)

    print('Reached end of main.')
    
def write(name):

    fileName = 'sim' + name + '.root'
    sim = TFile.Open(fileName, 'RECREATE')

    #if name is 'HDECAY':

    data = np.loadtxt(name + '/br.sm2', skiprows = 2)

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

    #if 'HDECAY' in fileName:

    canvas = TCanvas('Canvas', '', 600, 600)
    canvas.SetMargin(0.2, 0.1, 0.1, 0.1)
    canvas.cd()
    
    sim = TFile.Open(fileName, 'READ')
    massTree = sim.Get('massTree')
    widthTree = sim.Get('widthTree')

    m, w = array('f'), array('f')
    massLeaf = massTree.GetLeaf('m')
    widthLeaf = widthTree.GetLeaf('w')

    N = massTree.GetEntries()
    m125, w125 = array('f'), array('f')

    for i in range(N):
        massTree.GetEntry(i)
        m.append(massLeaf.GetValue())
        widthTree.GetEntry(i)
        w.append(widthLeaf.GetValue())
        if m[i] == 125:
            m125.append(125)
            w125.append(w[i])

    graph = TMultiGraph()

    graph0 = TGraph(N, m, w)
    #graph.Draw('A*')
    graph.Add(graph0)

    graph1 = TGraph(1, m125, w125)
    graph1.SetMarkerColor(3)
    graph.Add(graph1)

    graph.Draw('A*')

    graph.SetTitle('HDECAY mass-width plot')
    graph.GetXaxis().SetTitle('Higgs mass')
    graph.GetXaxis().CenterTitle(True)
    graph.GetYaxis().SetTitle('Decay width')
    graph.GetYaxis().CenterTitle(True)
    graph

    canvas.Print('graph' + fileName + '.png')

    #else: print('Not HDECAY')

if __name__ == '__main__': main()