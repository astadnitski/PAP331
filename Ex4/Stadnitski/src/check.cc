#include "../include/track.h"
using namespace std;

int main(int argc, char** argv) {

  track0 measurement0;
  measurement0.setMomentum(1, 1, 1, 1);

  float t = measurement0.getTransverse();
  cout << "- Transverse momentum: " << t << endl;

  float p = measurement0.getPseudo();
  cout << "- Pseudorapidity: " << p << endl;

  track1 measurement1;
  measurement1.setMomentum(2, 2, 2, 2);

  measurement1.setParticleID(3);
  cout << "- Particle ID: " << measurement1.getParticleID() << endl;

  measurement1.setParentID(4);
  cout << "- Parent ID: " << measurement1.getParentID() << endl;

}
