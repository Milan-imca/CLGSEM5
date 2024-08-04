#include<iostream>
#include<string>

using namespace std;



string encrypt(string plaintext,int shift){
  string cipherText = "";
  for(char currentChar : plaintext){
    if(currentChar == ' '){
      cipherText += currentChar;
    }
    else{
      char base = islower(currentChar) ? 'a' : 'A';
      char newChar = (currentChar + shift - base) % 26 + base;
      cipherText += newChar;
    }
  }
  return cipherText;
}
string decrypt(string cipherText,int shift){
  string plaintext = "";
  for(char currentChar : cipherText){
    if(currentChar == ' '){
      plaintext += currentChar;
    }
    else{
      char base = islower(currentChar) ? 'a' : 'A';
      char newChar = (currentChar - shift+26 - base) % 26 + base;
      plaintext += newChar;
    }
  }
  return plaintext;
}

int main(){
  string plaintext;
  string encryptedText;
  string decryptedText;
  int shift;

  cout<<"Enter the plaintext : ";
  getline(cin,plaintext);

  cout<<"Enter shift : ";
  cin>>shift;

  cout<<"Plain text : "<<plaintext<<endl;

  encryptedText = encrypt(plaintext,shift);
  cout<<"Encrypted Text -  " << encryptedText << endl;

  decryptedText = decrypt(encryptedText,shift);
  cout<<"Decrypted Text -  " << decryptedText << endl;


}