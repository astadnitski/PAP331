void makeplot() {

    TFile* normals = TFile::Open("normals.root", "READ");
    TTree* tree = (TTree*) normals -> Get("tree");
    TH1F* hist = new TH1F("hist", "Standard Gaussian, N = 1000", 100, -4, 4);

    Float_t n;
    tree -> SetBranchAddress("n", &n);
    int N = tree -> GetEntries();
    
    for (int i = 0; i < N; i++) {
        tree -> GetEntry(i);
        hist -> Fill(n);
    }

    hist -> SetFillColor(5);
    hist -> SetLineColor(1);
    hist -> SetLineWidth(3);

    hist -> GetXaxis() -> SetTitle("Simulated variable");
    hist -> GetXaxis() -> CenterTitle(true);
    hist -> GetYaxis() -> SetTitle("Number of hits");
    hist -> GetYaxis() -> CenterTitle(true);

    hist -> SetStats(0);
    hist -> Draw();

}