void Transverse-momentum-histogram()
{
//=========Macro generated from canvas: Canvas/
//=========  (Thu Mar 30 23:26:21 2023) by ROOT version 6.24/06
   TCanvas *Canvas = new TCanvas("Canvas", "",0,0,600,600);
   Canvas->SetHighLightColor(2);
   Canvas->Range(0,0,1,1);
   Canvas->SetFillColor(0);
   Canvas->SetBorderMode(0);
   Canvas->SetBorderSize(2);
   Canvas->SetFrameBorderMode(0);
   
   TH1F *hist__1 = new TH1F("hist__1","Transverse-momentum distribution, N = 1000",100,0,1404);
   hist__1->SetBinContent(1,689);
   hist__1->SetBinContent(2,149);
   hist__1->SetBinContent(3,57);
   hist__1->SetBinContent(4,33);
   hist__1->SetBinContent(5,17);
   hist__1->SetBinContent(6,7);
   hist__1->SetBinContent(7,11);
   hist__1->SetBinContent(8,4);
   hist__1->SetBinContent(9,3);
   hist__1->SetBinContent(10,4);
   hist__1->SetBinContent(11,3);
   hist__1->SetBinContent(12,2);
   hist__1->SetBinContent(13,6);
   hist__1->SetBinContent(14,2);
   hist__1->SetBinContent(15,2);
   hist__1->SetBinContent(16,1);
   hist__1->SetBinContent(27,1);
   hist__1->SetBinContent(28,2);
   hist__1->SetBinContent(30,1);
   hist__1->SetBinContent(31,1);
   hist__1->SetBinContent(35,2);
   hist__1->SetBinContent(45,1);
   hist__1->SetBinContent(64,1);
   hist__1->SetBinContent(100,1);
   hist__1->SetEntries(1000);
   hist__1->SetStats(0);
   hist__1->SetFillColor(7);
   hist__1->GetXaxis()->SetTitle("Transverse-momentum");
   hist__1->GetXaxis()->CenterTitle(true);
   hist__1->GetXaxis()->SetLabelFont(42);
   hist__1->GetXaxis()->SetTitleOffset(1);
   hist__1->GetXaxis()->SetTitleFont(42);
   hist__1->GetYaxis()->SetTitle("Number of events");
   hist__1->GetYaxis()->CenterTitle(true);
   hist__1->GetYaxis()->SetLabelFont(42);
   hist__1->GetYaxis()->SetTitleFont(42);
   hist__1->GetZaxis()->SetLabelFont(42);
   hist__1->GetZaxis()->SetTitleOffset(1);
   hist__1->GetZaxis()->SetTitleFont(42);
   hist__1->Draw("");
   Canvas->Modified();
   Canvas->cd();
   Canvas->SetSelected(Canvas);
}
