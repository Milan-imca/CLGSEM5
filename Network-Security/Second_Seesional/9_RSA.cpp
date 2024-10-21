#include <iostream>
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

// Function for modular exponentiation (a^b % mod)
int modExp(int base, int exp, int mod)
{
    int result = 1;
    base = base % mod;  // Take base modulo mod to prevent overflow
    while (exp > 0)
    {
        if (exp % 2 == 1)  // If exp is odd
            result = (result * base) % mod;
        exp = exp >> 1;  // exp = exp / 2
        base = (base * base) % mod;  // Square the base
    }
    return result;
}

int main()
{
    // Two prime numbers
    int p = 13, q = 21;
    int n = p * q, phi = (p - 1) * (q - 1), e = 13;

    // Ensure e and phi are coprime
    while (gcd(e, phi) != 1)
        e++;

    // Calculate d (modular inverse of e)
    int d = 1;
    while ((d * e) % phi != 1)
        d++;

    int message = 13;  // Message to be encrypted

    // Encrypt the message
    int c = modExp(message, e, n);  // Modular exponentiation for encryption
    // Decrypt the message
    int m = modExp(c, d, n);        // Modular exponentiation for decryption

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
