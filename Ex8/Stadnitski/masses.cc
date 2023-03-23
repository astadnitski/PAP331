#include "Pythia8/Pythia.h"
using namespace Pythia8;
using namespace std;

int main() {
    
    /// STEP 1: INITIALIZATION ///

    Pythia pythia;
    
    // Centre-of-mass energy: 13 TeV
    pythia.readString("Beams:eCM = 13000.");

    // Generate SM Higgs events
    pythia.readString("HiggsSM:all = on");
    pythia.readString("PhaseSpace:mHatMin = 100.");
    pythia.readString("Next:numberShowEvent = 0");

    // From documentation
    int HiggsID = 25;

    // Read in external PDF
    //pythia.readString("PDF:pSet = LHAPDF6:cteq6l1");

    pythia.init();

    /// STEP 2: EVENT GENERATION LOOP ///
    /// STEP 3: PRINT AND SAVE DATA ///

    for (int i = 0; i < 1000; ++i) {
        if (!pythia.next()) continue;
        int select = 0;
        for (int j = 0; j < pythia.event.size(); j++) if (pythia.event[j].id() == HiggsID) select = j;
        cout << i << " : Measured Higgs mass : " << pythia.event[select].m() << endl;
    }

    return 0;

}