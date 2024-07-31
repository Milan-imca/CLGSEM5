#include <iostream>
#include <string>
using namespace std;

// Function to encrypt the plaintext using the Vigenère cipher
string encryptVigenere(string plaintext, string keyword)
{
  string ciphertext = "";
  int keywordLength = keyword.length();
  int keywordIndex = 0;

  for (int i = 0; i < plaintext.length(); ++i)
  {
    char plainChar = plaintext[i];

    // Check if the character is a letter
    if (isalpha(plainChar))
    {
      char keyChar = keyword[keywordIndex % keywordLength];
      int shift = toupper(keyChar) - 'A';

      // Encrypt the character
      if (isupper(plainChar))
      {
        ciphertext += (plainChar - 'A' + shift) % 26 + 'A';
      }
      else
      {
        ciphertext += (plainChar - 'a' + shift) % 26 + 'a';
      }

      // Move to the next character in the keyword
      keywordIndex++;
    }
    else
    {
      // If it's not a letter, leave it unchanged
      ciphertext += plainChar;
    }
  }

  return ciphertext;
}

// Function to decrypt the ciphertext using the Vigenère cipher
string decryptVigenere(string ciphertext, string keyword)
{
  string plaintext = "";
  int keywordLength = keyword.length();
  int keywordIndex = 0;

  for (int i = 0; i < ciphertext.length(); ++i)
  {
    char cipherChar = ciphertext[i];

    // Check if the character is a letter
    if (isalpha(cipherChar))
    {
      char keyChar = keyword[keywordIndex % keywordLength];
      int shift = toupper(keyChar) - 'A';

      // Decrypt the character
      if (isupper(cipherChar))
      {
        plaintext += (cipherChar - 'A' - shift + 26) % 26 + 'A';
      }
      else
      {
        plaintext += (cipherChar - 'a' - shift + 26) % 26 + 'a';
      }

      // Move to the next character in the keyword
      keywordIndex++;
    }
    else
    {
      // If it's not a letter, leave it unchanged
      plaintext += cipherChar;
    }
  }

  return plaintext;
}

int main()
{
  string plaintext, keyword, ciphertext, decryptedText;

  cout << "Enter the plaintext: ";
  getline(cin, plaintext);

  cout << "Enter the keyword: ";
  cin >> keyword;

  // Encrypt the plaintext
  ciphertext = encryptVigenere(plaintext, keyword);
  cout << "Ciphertext: " << ciphertext << endl;

  // Decrypt the ciphertext
  decryptedText = decryptVigenere(ciphertext, keyword);
  cout << "Decrypted text: " << decryptedText << endl;

  return 0;
}
