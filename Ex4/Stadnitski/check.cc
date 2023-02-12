//#include "../include/track.h"
#include "include/track.h"
using namespace std;

int main(int argc, char** argv) {

  track measurement;
  measurement.setMomentum(3, 3, 3, 3);

  float t = measurement.getTransverse();
  cout << "Transverse momentum: " << t << endl;

  float p = measurement.getPseudo();
  cout << "Pseudorapidity: " << p << endl;

}
