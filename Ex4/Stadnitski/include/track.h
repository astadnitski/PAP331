#ifndef TRACK_H
#define TRACK_H

#include <cmath>
#include <iostream>
using namespace std;

class track0 {

protected: float E; float px; float py; float pz;

public:

  track0() { cout << "Constructor > memory allocated" << endl; }
  ~track0() { cout << "Destructor > memory released" << endl; }

  void setMomentum(float a0, float a1, float a2, float a3) {
    E = a0;
    px = a1;
    py = a2;
    pz = a3;
    cout << "- 4-momentum vector: (" << E << ", " << px << ", " << py << ", " << pz << ")" << endl;
  }

  float getTransverse() { return sqrt(pow(px, 2) + pow(py, 2)); }

  float getPseudo() {
    float r = sqrt(pow(px, 2) + pow(py, 2) + pow(pz, 2));
    float theta = acos(pz / r);
    /// cout << r << " | " << theta << endl;
    return -1 * log(tan(theta / 2));
  }

  virtual void setParticleID() {}
  virtual void setParentID() {}

  virtual int getParticleID() { return 0; }
  virtual int getParentID() { return 0; }

};

class track1: public track0 {

private: int particleID; int parentID;

public:

  void setParticleID(int a) { particleID = a; }
  void setParentID(int a) { parentID = a; }

  int getParticleID() { return particleID; }
  int getParentID() { return parentID; }

};

#endif
