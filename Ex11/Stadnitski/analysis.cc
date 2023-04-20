#include <iostream>
#include "TFile.h"
#include "TSelector.h"
#include "TTree.h"
using namespace std;

int main() {

    TFile* data = TFile::Open("DYJetsToLL.root", "READ");
    TTree* tree = (TTree*) data -> Get("Events");
    tree -> MakeSelector("selector");

    cout << "Reached end of main" << endl;

    return 0;

}