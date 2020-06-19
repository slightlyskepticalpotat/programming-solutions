#include <iostream>
#include <set>
using namespace std;
int number_gates, number_planes; // 4, 3

int main() {
  cin >> number_gates;
  cin >> number_planes;
  set<int> gates; // binary search tree (ordered set)
  int plane;
  for (int i = 1; i <= number_gates; i++) // insert gate numbers 
  {
    gates.insert(-i); // reverse gate order so largest first (-1, -2, -3, -4)
  }
  for (int j = 0; j < number_planes; j++)
  {
    cin >> plane;
    plane = -1 * plane; // make plane match gate (-4, -1)
    if(gates.lower_bound(plane) == gates.end()) // if only the smallest gate is left, print how many planes landed (-1)
    {
      cout << j << "\n"; // (2)
      return 0;
    }
    gates.erase(gates.lower_bound(plane)); // delete the used gates (-4)
  }
  cout << number_planes << "\n"; // if all planes were able to land
  return 0;
}