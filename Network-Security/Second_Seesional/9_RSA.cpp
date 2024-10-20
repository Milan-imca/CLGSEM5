#include <iostream>
#include <cmath>
using namespace std;

// Function to calculate gcd
int gcd(int a, int b)
{
  while (b)
  {
    a %= b;
    swap(a, b);
  }
  return a;
}

int main()
{
  // Two prime numbers
  int p = 13, q = 11;
  int n = p * q, phi = (p - 1) * (q - 1), e = 7;

  // Ensure e and phi are coprime
  while (gcd(e, phi) != 1)
    e++;

  // Calculate d (modular inverse of e)
  int d = 1;
  while ((d * e) % phi != 1)
    d++;

  int message = 9;
  int c = (int)pow(message, e) % n; // Encrypt
  int m = (int)pow(c, d) % n;       // Decrypt

  // Output the results
  cout << "Original Message = " << message << "\n"
       << "p = " << p << "\n"
       << "q = " << q << "\n"
       << "n = pq = " << n << "\n"
       << "phi = " << phi << "\n"
       << "e = " << e << "\n"
       << "d = " << d << "\n"
       << "Encrypted message = " << c << "\n"
       << "Decrypted message = " << m << "\n";

  // Check if the decrypted message matches the original message
  if (m == message)
  {
    cout << "RSA worked successfully!" << endl;
  }
  else
  {
    cout << "Error: RSA failed!" << endl;
  }

  return 0;
}
