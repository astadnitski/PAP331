#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

struct matrix { float mtx[2][2]; };

class measure {

private:
  float x;
  float y;
  vector <float> refX;
  vector <float> refY;

public:

  void setX(float a) { x = a; }
  void setY(float a) { y = a; }

  float getX() { return x; }
  float getY() { return y; }

  void setRefX(vector <float> a) { refX = a; }
  void setRefY(vector <float> a) { refY = a; }

  float vectorSum(vector <float> a) {
    float sum = 0;
    for (int i = 0; i < a.size(); i++) sum += a.at(i);
    return sum;
  }

  float variance(vector <float> a) {
    float avg = vectorSum(a) / a.size();
    float sum;
    for (int i = 0; i < a.size(); i++) sum += pow(a.at(i) - avg, 2);
    return sum / 9;
  }

  float covariance(vector <float> a, vector <float> b) {
    vector <float> ab {};
    for (int i = 0; i < a.size(); i++) ab.push_back(a.at(i) * b.at(i));
    float sumAB = vectorSum(ab);
    float sumA = vectorSum(a);
    float sumB = vectorSum(b);
    return (sumAB - (sumA * sumB / a.size())) / a.size();
  }

  matrix getError(float a, float b) {
    matrix err;
    err.mtx[0][0] = variance(refX);
    err.mtx[0][1] = covariance(refX, refY);
    err.mtx[1][0] = covariance(refX, refY);
    err.mtx[1][1] = variance(refY);
    return err;
  }

  float getDist(float a, float b) { return sqrt(pow(a, 2) + pow(b, 2)); }

  float getDistErr(float a, float b) {
    float dist = getDist(a, b);
    matrix err = getError(a, b);
    float varX = err.mtx[0][0];
    float varY = err.mtx[1][1];
    return sqrt(pow(a / dist, 2) * varX + pow(b / dist, 2) * varY + 2 * a * b * err.mtx[0][1] / pow(dist, 2));
  }

  float getSig(float a, float b) { return getDist(a, b) / getDistErr(a, b); }

};
