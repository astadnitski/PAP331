#include "../include/track.h"
using namespace std;

int main(int argc, char** argv) {

  /// Testing class functionality with some made-up numbers
  cout << "Testing base class" << endl;

  track0 measurement0;
  measurement0.setMomentum(1, 1, 1, 1);
  cout << "- Transverse momentum: " << measurement0.getTransverse() << endl;
  cout << "- Pseudorapidity: " << measurement0.getPseudo() << endl;

  cout << "Testing inheriting class" << endl;

  /// For simulated particle:
  /// - Transverse momentum should be doubled (2x magnitude in X-Y)
  /// - Pseudorapidity should be same (different magnitude, same argument)
  track1 measurement1;
  measurement1.setMomentum(2, 2, 2, 2);
  cout << "- Transverse momentum: " << measurement1.getTransverse() << endl;
  cout << "- Pseudorapidity: " << measurement1.getPseudo() << endl;

  /// More made-up numbers for the ID fields
  measurement1.setParticleID(3);
  cout << "- Particle ID: " << measurement1.getParticleID() << endl;
  measurement1.setParentID(4);
  cout << "- Parent ID: " << measurement1.getParentID() << endl;

}
