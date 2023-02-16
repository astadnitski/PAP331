#include "../include/track.h"
using namespace std;

/// Base class: constructor
track0::track0() {
  E = 0;
  px = 0;
  py = 0;
  pz = 0;
}

/// Base class: destructor
track0::~track0() {}

/// Defining the 4-momentum
void track0::setMomentum(float a0, float a1, float a2, float a3) {
  E = a0;
  px = a1;
  py = a2;
  pz = a3;
  cout << "- 4-momentum vector: (" << E << ", " << px << ", " << py << ", " << pz << ")" << endl;
}

/// Getters
float track0::getTransverse() { return sqrt(pow(px, 2) + pow(py, 2)); }
float track0::getPseudo() {
  float r = sqrt(pow(px, 2) + pow(py, 2) + pow(pz, 2));
  float theta = acos(pz / r);
  return -1 * log(tan(theta / 2));
}

/// Inheriting class: constructor
track1::track1() {
  E = 0;
  px = 0;
  py = 0;
  pz = 0;
}

/// Inheriting class: destructor
track1::~track1() {  }

/// Overriding virtual functions from the header
void track1::setParticleID(int a) { particleID = a; }
void track1::setParentID(int a) { parentID = a; }
int track1::getParticleID() { return particleID; }
int track1::getParentID() { return parentID; }
