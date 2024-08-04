// Verman cipher / One Time Pad Cipher:

#include <iostream>
#include <string>

using namespace std;

// Function to convert a character to its corresponding 0-25 value
int charToValue(char c)
{
  return c - 'A';
}

// Function to convert a 0-25 value to its corresponding character
char valueToChar(int v)
{
  return v + 'A';
}

// Function to encrypt plaintext using Vernam cipher (one-time pad)
string vernamEncrypt(string plaintext, string key)
{
  string ciphertext = "";
  for (int i = 0; i < plaintext.length(); i++)
  {
    int pVal = charToValue(plaintext[i]);
    int kVal = charToValue(key[i]);
    int cVal = (pVal + kVal) % 26; // Wrap around using modulo 26
    ciphertext += valueToChar(cVal);
  }
  return ciphertext;
}

// Function to decrypt ciphertext using Vernam cipher (one-time pad)
string vernamDecrypt(string ciphertext, string key)
{
  string plaintext = "";
  for (int i = 0; i < ciphertext.length(); i++)
  {
    int cVal = charToValue(ciphertext[i]);
    int kVal = charToValue(key[i]);
    int pVal = (cVal - kVal + 26) % 26; // Wrap around using modulo 26
    plaintext += valueToChar(pVal);
  }
  return plaintext;
}

int main()
{
  string plaintext = "ATTACK";
  string key = "CZVCBO";

  string ciphertext = vernamEncrypt(plaintext, key);
  string decryptedText = vernamDecrypt(ciphertext, key);

  cout << "Plaintext: " << plaintext << endl;
  cout << "Key: " << key << endl;
  cout << "Cipher Text: " << ciphertext << endl;
  cout << "Decrypted Text: " << decryptedText << endl;

  return 0;
}
