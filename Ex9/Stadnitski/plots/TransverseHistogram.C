void TransverseHistogram()
{
//=========Macro generated from canvas: Canvas/
//=========  (Thu Mar 30 11:44:41 2023) by ROOT version 6.24/06
   TCanvas *Canvas = new TCanvas("Canvas", "",0,0,600,600);
   Canvas->SetHighLightColor(2);
   Canvas->Range(0,0,1,1);
   Canvas->SetFillColor(0);
   Canvas->SetBorderMode(0);
   Canvas->SetBorderSize(2);
   Canvas->SetFrameBorderMode(0);
   
   TH1F *hist__1 = new TH1F("hist__1","Transverse momenta, N = 1000",100,0,1600);
   hist__1->SetBinContent(1,718);
   hist__1->SetBinContent(2,142);
   hist__1->SetBinContent(3,53);
   hist__1->SetBinContent(4,27);
   hist__1->SetBinContent(5,10);
   hist__1->SetBinContent(6,13);
   hist__1->SetBinContent(7,4);
   hist__1->SetBinContent(8,5);
   hist__1->SetBinContent(9,3);
   hist__1->SetBinContent(10,3);
   hist__1->SetBinContent(11,4);
   hist__1->SetBinContent(12,4);
   hist__1->SetBinContent(13,3);
   hist__1->SetBinContent(15,1);
   hist__1->SetBinContent(24,1);
   hist__1->SetBinContent(25,2);
   hist__1->SetBinContent(27,1);
   hist__1->SetBinContent(28,1);
   hist__1->SetBinContent(31,2);
   hist__1->SetBinContent(40,1);
   hist__1->SetBinContent(57,1);
   hist__1->SetBinContent(88,1);
   hist__1->SetEntries(1000);
   hist__1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   hist__1->SetLineColor(ci);
   hist__1->GetXaxis()->SetLabelFont(42);
   hist__1->GetXaxis()->SetTitleOffset(1);
   hist__1->GetXaxis()->SetTitleFont(42);
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
