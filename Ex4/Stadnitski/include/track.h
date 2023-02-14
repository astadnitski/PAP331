#ifndef TRACK_H
#define TRACK_H

#include <cmath>
#include <iostream>
using namespace std;

class track0 {

protected: float E; float px; float py; float pz;

public:

  track0(); ~track0();

  void setMomentum(float a0, float a1, float a2, float a3);

  float getTransverse();
  float getPseudo();

  virtual void setParticleID() {}
  virtual void setParentID() {}

  virtual int getParticleID() { return 0; }
  virtual int getParentID() { return 0; }

};


class track1: public track0 {

private: int particleID; int parentID;

public:

  track1(); ~track1();

  void setParticleID(int a);
  void setParentID(int a);

  int getParticleID();
  int getParentID();

};

#endif
