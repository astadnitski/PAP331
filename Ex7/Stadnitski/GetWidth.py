#/usr/bin/env python
from array import array
import numpy as np
from ROOT import *

def main():

    HDECAY = write('HDECAY')
    #draw(HDECAY)

    FEYNHIGGS = write('FEYNHIGGS')
    draw('both')
    
def write(name):

    sim = TFile.Open('sim' + name + '.root', 'RECREATE')

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
    
    return name

def read(name, color):

    sim = TFile.Open('sim' + name + '.root', 'READ')
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

    graph0 = TGraph(N, m, w)
    graph0.SetMarkerColor(color)

    graph1 = TGraph(1, m125, w125)
    graph1.SetMarkerColor(1)

    return graph0, graph1

def draw(mode):

    name = ''

    canvas = TCanvas('Canvas', '', 600, 600)
    canvas.SetMargin(0.2, 0.1, 0.1, 0.1)
    canvas.cd()
    
    graph = TMultiGraph()

    graphHD0, graphHD1 = read('HDECAY', 2)
    graphHD0.SetName('hd')
    graph.Add(graphHD0)
    graph.Add(graphHD1)

    if mode is 'both':
        graphFH0, graphFH1 = read('FEYNHIGGS', 4)
        graphFH0.SetName('fh')
        graph.Add(graphFH0)
        graph.Add(graphFH1)

    graph.Draw('A*')

    graph.SetTitle(name + ' Mass-width plot')
    graph.GetXaxis().SetTitle('Higgs mass')
    graph.GetXaxis().CenterTitle(True)
    graph.GetYaxis().SetTitle('Decay width')
    graph.GetYaxis().CenterTitle(True)

    legend = TLegend(0.7, 0.2, 0.9, 0.3)
    legend.AddEntry('fh', 'FeynHiggs')
    legend.AddEntry('hd', 'HDECAY')
    legend.Draw()

    canvas.Print('graph' + name + '.png')

if __name__ == '__main__': main()