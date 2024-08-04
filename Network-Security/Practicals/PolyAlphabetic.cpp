#include<iostream>
#include<string>

using namespace std;

string encrypt(string plaintext,string key){
  string cipherText = "";
  int keyLength = key.length();
  int keyIndex = 0;

  for(char currChar : plaintext){
    if(isalpha(currChar)){
      char base = isupper(currChar) ? 'A' : 'a';
      char keyChar = key[keyIndex % keyLength];
      char keyBase = isupper(keyChar)? 'A' : 'a';
      int shift = toupper(keyChar) - 'A';

      int currCharPos = currChar - base;
      int newCharPos = (currCharPos + shift) % 26;
      char newChar = newCharPos + base;

      cipherText += newChar;
      keyIndex++;
    }
    else{
      cipherText += currChar;
    }
  }
  return cipherText;
}

string decrypt(string plaintext,string key){
  string cipherText = "";
  int keyLength = key.length();
  int keyIndex = 0;

  for(char currChar : plaintext){
    if(isalpha(currChar)){
      char base = isupper(currChar) ? 'A' : 'a';
      char keyChar = key[keyIndex % keyLength];
      char keyBase = isupper(keyChar)? 'A' : 'a';
      int shift = toupper(keyChar) - 'A';

      int currCharPos = currChar - base;
      int newCharPos = (currCharPos - shift + 26) % 26;
      char newChar = newCharPos + base;

      cipherText += newChar;
      keyIndex++;
    }
    else{
      cipherText += currChar;
    }
  }
  return cipherText;
}

int main(){
  string plaintext = "HELLO";
  string key = "HEY";

  cout<<"Plain text : " << plaintext << endl;
  string cipherText = encrypt(plaintext,key);
  cout<<"CipherText : "<<cipherText<<endl;

  cout<<"Decrpted Text : " <<decrypt(cipherText,key);

}