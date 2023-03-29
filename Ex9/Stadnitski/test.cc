#include "Pythia8/Pythia.h"
using namespace Pythia8;
using namespace std;

int main() {
    
    /// STEP 1: INITIALIZATION ///

    Pythia pythia;

    pythia.readString("Beams:eCM = 13000.");
    pythia.readString("Next:numberShowEvent=0");
    pythia.init();
    
    /// STEP 2: EVENT GENERATION LOOP ///
    /// STEP 3: PRINT AND SAVE DATA ///

    cout << "Hello" << endl;
    return 0;

}