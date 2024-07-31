#include <iostream>

using namespace std;

string encrypt(string text, int s)
{
  string result = "";
  for (char c : text)
  {
    if (isalpha(c))
    {
      char base = isupper(c) ? 'A' : 'a';
      result += char((c + s - base) % 26 + base);
    }
    else
    {
      result += c;
    }
  }
  return result;
}

string decrypt(string text, int s)
{
  string result = "";
  for (char c : text)
  {
    if (isalpha(c))
    {
      char base = isupper(c) ? 'A' : 'a';
      result += char((c - s - base + 26) % 26 + base);
    }
    else
    {
      result += c;
    }
  }
  return result;
}

int main()
{
  string plainText;
  int shift;

  cout << "Enter the plain text : ";
  cin >> plainText;

  cout << "Enter the shift value : ";
  cin >> shift;

  cout << "Plain Text : " << plainText << endl;

  string cipherText = encrypt(plainText, shift);
  cout << "Encrypted: " << cipherText << endl;

  string decryptedText = decrypt(cipherText, shift);
  cout << "Decrypted: " << decryptedText << endl;

  return 0;
}
