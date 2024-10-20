#include<iostream>
#include<string>
// #include<cctype>

using namespace std;

string encrypt(string plaintext,char key[]){
  string cipherText = "";

  for(char currChar : plaintext){
    if(currChar == ' '){
      cipherText += currChar;
    }
    else{
      char base = islower(currChar) ? 'a' : 'A';
      int index = currChar - base;
      cipherText += islower(currChar) ? tolower(key[index]) : toupper(key[index]);
    }
  }
  return cipherText;
}


string decrypt(string cipherText,char key[]){
  string plaintext = "";
  for(char currChar : cipherText){
    if(currChar == ' '){
      cipherText += currChar;
    }
    else{
      // condition ? true : false;
      char base = islower(currChar)? 'a' : 'A';
      char keyChar = isupper(currChar)?tolower(currChar):currChar;
      int index = 0;
      while(index < 25 && key[index] != keyChar){
        index++;
      }
      plaintext += base + index;
    }
  }
  return plaintext;
}

int main(){

  string plaintext = "hello";
  string encryptedText;
  string decryptedText;
  char key[26] = {'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'};

  cout<<"Plain text : "<<plaintext<<endl;

  encryptedText = encrypt(plaintext,key);
  cout<<"Encrypted Text : "<<encryptedText << endl;

  decryptedText = decrypt(encryptedText,key);
  cout<<"Decrypted Text : " <<decryptedText << endl;
}
