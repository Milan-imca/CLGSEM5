#include<iostream>
#include<string>
using namespace std;


string encrypt(string plaintext,int shift){
  string cipherText = "";
  for(char currChar : plaintext){
    if(currChar == ' '){
      cipherText += currChar;
    }
    else{
      char base = islower(currChar)? 'a' : 'A';
      char newChar = (currChar + shift - base ) % 26 + base;
      cipherText += newChar;
    }
  }
  return cipherText;
}

string decrypt(string cipherText,int shift){
  string plaintext = "";
  for(char currChar : cipherText){
    if(currChar == ' '){
      plaintext += currChar;
    }
    else{
      char base = islower(currChar)? 'a' : 'A';
      char newChar = (currChar - shift+26 - base ) % 26 + base;
      plaintext += newChar;
    }
  }
  return plaintext;
}

int main(){
  string plaintext;
  int shift = 3;

  cout<<"Enter plaintext : ";
  getline(cin,plaintext);

  string encryptedText = encrypt(plaintext,shift);
  cout<<"Encrpted text : "<<encryptedText<<endl;


  string decryptedText = decrypt(encryptedText,shift);
  cout<<"Decrypted text : "<<decryptedText<<endl;

}