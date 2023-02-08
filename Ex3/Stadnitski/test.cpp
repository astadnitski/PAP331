#include <measure>

int main(int argc, char** argv) {

  measure measurement;

  float x0;
  cout << "Enter x: "; cin >> x0;
  measurement.setX(x0);

  float y0;
  cout << "Enter y: "; cin >> y0;
  measurement.setY(y0);

  float x = measurement.getX();
  float y = measurement.getY();
  matrix error = measurement.getError(x, y);

  cout << "Measurement: (" << x << ", " << y << ")" << endl;
  cout << "Error matrix" << endl;
  cout << error.mtx[0][0] << " | " << error.mtx[0][1] << endl;
  cout << error.mtx[1][0] << " | " << error.mtx[1][1] << endl;
  cout << "Distance: " << measurement.getDist(x, y) << " +/- " << measurement.getDistErr(x, y) << endl;
  cout << "Significance: " << measurement.getSig(x, y) << endl;

}
