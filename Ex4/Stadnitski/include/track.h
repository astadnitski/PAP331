#ifndef TRACK_H
#define TRACK_H

#include <cmath>
#include <iostream>
using namespace std;

class track {

private:
  float E; float px; float py; float pz;

public:

  void setMomentum(float a0, float a1, float a2, float a3) {
    E = a0;
    px = a1;
    py = a2;
    pz = a3;
  }

  float getTransverse() { return sqrt(pow(px, 2) + pow(py, 2)); }

  float getPseudo() {
    float r = sqrt(pow(px, 2) + pow(py, 2) + pow(pz, 2));
    float theta = acos(pz / r);
    //cout << r << " | " << theta << endl;
    return -1 * log(tan(theta / 2));
  }

};

#endif
