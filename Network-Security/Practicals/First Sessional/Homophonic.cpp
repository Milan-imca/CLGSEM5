#include <iostream>
#include <unordered_map>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;


// mapping the each alphabet for to the random alphabets
unordered_map<char, vector<char>> generateHomphonicCipherMap()
{
  return {
      {'A', {'Q', 'W', 'E'}}, 
      {'B', {'R', 'T', 'Y'}}, 
      {'C', {'U', 'I', 'O'}}, 
      {'D', {'P', 'A', 'S'}}, 
      {'E', {'D', 'F', 'G'}}, 
      {'F', {'H', 'J', 'K'}}, 
      {'G', {'L', 'Z', 'X'}}, 
      {'H', {'C', 'V', 'B'}}, 
      {'I', {'N', 'M', 'Q'}}, 
      {'J', {'W', 'E', 'R'}}, 
      {'K', {'T', 'Y', 'U'}}, 
      {'L', {'I', 'O', 'P'}}, 
      {'M', {'A', 'S', 'D'}}, 
      {'N', {'F', 'G', 'H'}}, 
      {'O', {'J', 'K', 'L'}}, 
      {'P', {'Z', 'X', 'C'}}, 
      {'Q', {'V', 'B', 'N'}}, 
      {'R', {'M', 'Q', 'W'}}, 
      {'S', {'E', 'R', 'T'}}, 
      {'T', {'Y', 'U', 'I'}}, 
      {'U', {'O', 'P', 'A'}}, 
      {'V', {'S', 'D', 'F'}}, 
      {'W', {'G', 'H', 'J'}}, 
      {'X', {'K', 'L', 'Z'}}, 
      {'Y', {'X', 'C', 'V'}}, 
      {'Z', {'B', 'N', 'M'}}
  };
}
//Encrypting the plain text;
string encrypt(const string& plainText,const unordered_map<char,vector<char>>& cipherMap){
  string cipherText;
  srand(time(0));

  for(char c : plainText){
    if (isalpha(c)){
      c = toupper(c);
      const vector<char>& possibleChars = cipherMap.at(c);
      cipherText += possibleChars[rand() % possibleChars.size()];
    }
    else{
      cipherText += c;
    }
  }
  return cipherText;
}

int main() {
    unordered_map<char, vector<char>> cipherMap = generateHomphonicCipherMap();
    string plainText;
    cout << "Enter the plain text: ";
    getline(cin, plainText);

    // Encrypt the plaintext
    string encryptedText = encrypt(plainText, cipherMap);
    cout << "Encrypted text: " << encryptedText << endl;


    return 0;
}
