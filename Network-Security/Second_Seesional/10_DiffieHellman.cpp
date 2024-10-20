#include <iostream>
#include <cmath>
using namespace std;

// Function to calculate (g^h) % Ps
long long int powerMod(long long int g, long long int h, long long int Ps)
{
  return (long long int)pow(g, h) % Ps;
}

int main()
{
  // Public values
  long long int Ps = 32, Gs = 5, g = 6, h = 2;

  cout << "Value of Ps: " << Ps << "\nValue of Gs: " << Gs << endl;
  cout << "Private keys - g: " << g << ", h: " << h << endl;

  // Generate shared keys
  long long int p = powerMod(Gs, g, Ps); // Alen's public key
  long long int q = powerMod(Gs, h, Ps); // Roy's public key

  // Secret keys for Alen and Roy
  long long int K_A = powerMod(q, g, Ps); // Alen's secret key
  long long int K_B = powerMod(p, h, Ps); // Roy's secret key

  // Output results
  cout << "Alen's Secret Key: " << K_A << "\nRoy's Secret Key: " << K_B << endl;

  return 0;
}
