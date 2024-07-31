#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Function to encrypt the plaintext using Rail Fence Cipher
string encryptRailFence(const string &text, int key)
{
  if (key <= 1)
    return text;

  vector<string> rails(key);
  int direction = 1; // 1 for down, -1 for up
  int row = 0;

  for (char ch : text)
  {
    rails[row] += ch;
    row += direction;

    if (row == 0 || row == key - 1)
      direction = -direction;
  }

  string result;
  for (const string &rail : rails)
  {
    result += rail;
  }

  return result;
}

// Function to decrypt the ciphertext using Rail Fence Cipher
string decryptRailFence(const string &cipher, int key)
{
  if (key <= 1)
    return cipher;

  vector<string> rails(key);
  vector<int> railLengths(key, 0);
  int direction = 1; // 1 for down, -1 for up
  int row = 0;

  for (char ch : cipher)
  {
    railLengths[row]++;
    row += direction;

    if (row == 0 || row == key - 1)
      direction = -direction;
  }

  int index = 0;
  for (int i = 0; i < key; ++i)
  {
    rails[i] = cipher.substr(index, railLengths[i]);
    index += railLengths[i];
  }

  string result;
  row = 0;
  direction = 1;

  vector<int> railIndexes(key, 0);
  for (int i = 0; i < cipher.size(); ++i)
  {
    result += rails[row][railIndexes[row]++];
    row += direction;

    if (row == 0 || row == key - 1)
      direction = -direction;
  }

  return result;
}

int main()
{
  string text = "ATTACKATDAWN";
  int key = 2;

  string encrypted = encryptRailFence(text, key);
  cout << "Encrypted: " << encrypted << endl;

  string decrypted = decryptRailFence(encrypted, key);
  cout << "Decrypted: " << decrypted << endl;

  return 0;
}
