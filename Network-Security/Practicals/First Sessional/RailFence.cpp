#include <iostream>
#include <string>
#include <vector>

using namespace std;

string encrypt(string plainText, int key)
{
  if (key == 1)
    return plainText;

  int n = plainText.length();
  vector<vector<char>> rail(key, vector<char>(n, '\0'));

  // vector<vector<char>> rail(key,vector<char>(n,'\0'));

  bool dir_down = true;
  int row = 0, col = 0;

  for (int i = 0; i < n; i++)
  {
    rail[row][col++] = plainText[i];

    if (row == key - 1) // 0 == 1
      dir_down = false;
    else if (row == 0)
      dir_down = true;

    row += dir_down ? 1 : -1;
  }

  string cipherText;
  for (int i = 0; i < key; i++)
  {
    for (int j = 0; j < n; j++)
    {
      if (rail[i][j] != '\0')
        cipherText += rail[i][j];
    }
  }

  return cipherText;
}

string decrypt(string cipherText, int key)
{
  if (key == 1)
    return cipherText;

  int n = cipherText.length();
  vector<vector<char>> rail(key, vector<char>(n, '\0'));
  bool dir_down;
  int row = 0, col = 0;

  for (int i = 0; i < n; i++)
  {
    rail[row][col++] = '*';

    if (row == key - 1)
      dir_down = false;
    else if (row == 0)
      dir_down = true;

    row += dir_down ? 1 : -1;
  }

  int index = 0;
  for (int i = 0; i < key; i++)
  {
    for (int j = 0; j < n; j++)
    {
      if (rail[i][j] == '*' && index < n)
        rail[i][j] = cipherText[index++];
    }
  }

  string plainText;
  dir_down = true;
  row = 0, col = 0;

  for (int i = 0; i < n; i++)
  {
    plainText += rail[row][col++];

    if (row == key - 1)
      dir_down = false;
    else if (row == 0)
      dir_down = true;

    row += dir_down ? 1 : -1;
  }

  return plainText;
}

int main()
{
  string plainText, cipherText;
  int key;

  cout << "Enter plain text: ";
  getline(cin, plainText);
  cout << "Enter key: ";
  cin >> key;

  cipherText = encrypt(plainText, key);
  cout << "Cipher text: " << cipherText << endl;

  plainText = decrypt(cipherText, key);
  cout << "Decrypted text: " << plainText << endl;

  return 0;
}

