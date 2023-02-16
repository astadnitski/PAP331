#ifndef TRACK_H
#define TRACK_H

#include <cmath>
#include <iostream>
using namespace std;

/// Base class
class track0 {

/// Protected fields inherited by track1
protected: float E; float px; float py; float pz;

public:

  /// Constructor & destructor
  track0(); ~track0();

  /// Getters & setters
  void setMomentum(float a0, float a1, float a2, float a3);
  float getTransverse();
  float getPseudo();

  /// Virtual functions may be used differently in inheriting classes
  virtual void setParticleID() {}
  virtual void setParentID() {}
  virtual int getParticleID() { return 0; }
  virtual int getParentID() { return 0; }

};

/// Inheriting class
class track1: public track0 {

private: int particleID; int parentID;

public:

  /// Constructor & destructor
  track1(); ~track1();

  /// Using virtual functions from base class
  void setParticleID(int a);
  void setParentID(int a);
  int getParticleID();
  int getParentID();

};

#endif
