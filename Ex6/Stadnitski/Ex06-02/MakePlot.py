#/usr/bin/env python
from array import array
import ROOT

def main():

    canvas = ROOT.TCanvas('Canvas', '', 600, 600)
    canvas.SetFillColor(0)
    canvas.cd()
    
    normals = ROOT.TFile.Open('normals.root', 'READ')
    tree = normals.Get('tree')
    hist = ROOT.TH1F('hist', 'Standard Gaussian, N = 1000', 100, -4, 4)
    
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

    hist.SetStats(0)
    hist.Draw()

    canvas.Print('graph.C')
    canvas.Print('graph.eps')
    canvas.Print('graph.png')
    
    print('Reached end of main')

if __name__ == '__main__': main()