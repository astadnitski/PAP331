#include "Pythia8/Pythia.h"
using namespace Pythia8;
using namespace std;

int main() {
    
    /// STEP 1: INITIALIZATION ///

    Pythia pythia;
    pythia.readString("Beams:eCM = 13000.");
    pythia.readString("PhotonCollision:gmgm2mumu = on");
    //pythia.readString("SoftQCD:nonDiffractive = on");
    pythia.readString("Next:numberShowEvent=0");
    pythia.init();
    
    /// STEP 2: EVENT GENERATION LOOP ///

    Hist transverse("Transverse momentum", 100, -5., 5.);
    Hist pseudo("Pseudorapidity", 100, -5., 5.);
    for (int i = 0; i < 1000; i++) {
        if (!pythia.next()) continue;
        int select = 0;
        for (int j = 0; j < pythia.event.size(); j++) if (pythia.event[j].id() == 13) select = j;
        transverse.fill(pythia.event[select].pT());
        pseudo.fill(pythia.event[select].eta());
        cout << i << " : Transverse momentum : " << pythia.event[select].pT() << endl;
        cout << i << " : Pseudorapidity : " << pythia.event[select].eta() << endl;
        cout << endl;
    }

    /// STEP 3: PRINT AND SAVE DATA ///

    pythia.stat();
    cout << transverse;
    cout << pseudo;

    return 0;

}