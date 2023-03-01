#/usr/bin/env python
from array import array
import ROOT

def main():

    N = 1000
    rng = ROOT.TRandom()
    normals = ROOT.TFile.Open('normals.root', 'RECREATE');
    tree = ROOT.TTree('tree', 'Tree of normally distributed numbers');
    
    n = array('f', [0])
    tree.Branch('n', n, 'n/F')
    
    for i in range(N):
        n[0] = rng.Gaus(0, 1)
        tree.Fill()

    tree.Write()
    normals.Close()

    print('Saved numbers to ROOT file')

if __name__ == '__main__': main()