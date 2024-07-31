// credits to @PriyaShah

#include <iostream>
#include <string>

using namespace std;

int main()
{
  char key[26] = {'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'};

  string plainText;
  string cipherText;

  cout << "Enter the text : ";
  getline(cin, plainText);

  cout << "Entered Plain text : " << plainText;

  for (int i = 0; i < plainText.length(); i++)
  {
    if (plainText[i] == ' ')   
    {
      cipherText += plainText[i];
    }
    else
    {
      if (isupper(plainText[i]))
      {
        int num = int(plainText[i]);
        cipherText += toupper(key[num - 65]);
      }
      else
      {
        int num = int(plainText[i]);
        cipherText += key[num - 97];
      }
    }
  }

  cout << "Cipher Text : " << cipherText << endl;
}