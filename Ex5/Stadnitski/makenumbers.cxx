void makenumbers() {

    int N = 1000;
    TRandom* rng = new TRandom;
    TFile* normals = TFile::Open("normals.root", "RECREATE");
    TTree* tree = new TTree("tree", "Tree of normally distributed numbers");
    
    Float_t n;
    tree -> Branch("n", &n, "n/F");
    
    for (int i = 0; i < N; i++) {
        n = rng -> Gaus(0, 1);
        tree -> Fill();
    }
    
    tree -> Write();
    normals -> Close();
    exit(0);

}