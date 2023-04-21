#define selector_cxx

#include "selector.h"
#include <TH2.h>
#include <TH1F.h>
#include <TStyle.h>

int nN; int nD;
TH1F *h;

void selector::Begin(TTree * /*tree*/) {
   TString option = GetOption();
}

void selector::SlaveBegin(TTree * /*tree*/) {
   TString option = GetOption();
   h = new TH1F("nJet", "Pileup distribution", 60, 0, 60);
}

Bool_t selector::Process(Long64_t entry) {

   fReader.SetLocalEntry(entry);

   nD++;
   // Check if the event passes the trigger
   if (*HLT_IsoMu24) {
      nN++;
      h -> Fill(*PV_npvs);
   }

   return kTRUE;
}

void selector::SlaveTerminate() {}

void selector::Terminate() {

   TCanvas* canvas = new TCanvas("Canvas", "", 600, 600);
   canvas -> cd();

   float efficiency = float (nN) / nD;
   std::cout << "Trigger efficiency : " << efficiency << endl;

   h -> SetFillColor(3);
   h -> GetXaxis() -> SetTitle("Number of primary vertices");
   h -> GetXaxis() -> CenterTitle(true);
   h -> GetYaxis() -> SetTitle("Number of hits");
   h -> GetYaxis() -> CenterTitle(true);

   h -> Draw();
   h -> SetStats(0);

   canvas -> SaveAs("pileup.png");
   canvas -> SaveAs("pileup.pdf");
   canvas -> SaveAs("pileup.eps");

}