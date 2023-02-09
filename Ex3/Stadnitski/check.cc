#include "measure.h"
#include <fstream>
using namespace std;

int main(int argc, char** argv) {

  measure measurement;

  float x0;
  cout << "Enter x: "; cin >> x0;
  measurement.setX(x0);
  float x = measurement.getX();

  float y0;
  cout << "Enter y: "; cin >> y0;
  measurement.setY(y0);
  float y = measurement.getY();

  measurement.setRefX(vector <float> {7, 8, 6, 3, 0, 5, 4, 5, 5, 0}); // Ex2 pyOut
  measurement.setRefY(vector <float> {2, 6, 7, 3, 3, 2, 2, 8, 0, 1}); // Ex2 shOut % 9
  matrix error = measurement.getError(x, y);

  // There is surely a more efficient way to do both terminal output and text save but I haven't found it yet
  cout << "Measurement: (" << x << ", " << y << ")" << endl;
  cout << "Error matrix" << endl;
  cout << error.mtx[0][0] << " | " << error.mtx[0][1] << endl;
  cout << error.mtx[1][0] << " | " << error.mtx[1][1] << endl;
  cout << "Distance: " << measurement.getDist(x, y) << " +/- " << measurement.getDistErr(x, y) << endl;
  cout << "Significance: " << measurement.getSig(x, y) << endl;

  ofstream info; string filename = "measurement.txt";
  //info.open("measurement_" + to_string(x) + "_" + to_string(y) + ".txt");
  info.open(filename);
  info << "Measurement: (" << x << ", " << y << ")" << endl;
  info << "Error matrix" << endl;
  info << error.mtx[0][0] << " | " << error.mtx[0][1] << endl;
  info << error.mtx[1][0] << " | " << error.mtx[1][1] << endl;
  info << "Distance: " << measurement.getDist(x, y) << " +/- " << measurement.getDistErr(x, y) << endl;
  info << "Significance: " << measurement.getSig(x, y) << endl;
  info.close();

  cout << "Output saved to " << filename << endl;

}
