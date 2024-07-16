#include <iostream>
#include <string>

using namespace std;


string vernamEncrypt(const string& plaintext, const string& key) {
    string ciphertext = "";
    for (int i = 0; i < plaintext.length(); i++) {
        if (isupper(plaintext[i]) && isupper(key[i])) {
            char encryptedChar = ((plaintext[i] - 'A') + (key[i] - 'A')) % 26 + 'A';
            ciphertext += encryptedChar;
        } else if (islower(plaintext[i]) && islower(key[i])) {
            char encryptedChar = ((plaintext[i] - 'a') + (key[i] - 'a')) % 26 + 'a';
            ciphertext += encryptedChar;
        } else {
            ciphertext += plaintext[i];  
        }
    }
    return ciphertext;
}

string vernamDecrypt(const string& ciphertext, const string& key) {
    string decryptedText = "";
    for (int i = 0; i < ciphertext.length(); i++) {
        if (isupper(ciphertext[i]) && isupper(key[i])) {
            char decryptedChar = ((ciphertext[i] - 'A') - (key[i] - 'A') + 26) % 26 + 'A';
            decryptedText += decryptedChar;
        } else if (islower(ciphertext[i]) && islower(key[i])) {
            char decryptedChar = ((ciphertext[i] - 'a') - (key[i] - 'a') + 26) % 26 + 'a';
            decryptedText += decryptedChar;
        } else {
            decryptedText += ciphertext[i];  
    }
    return decryptedText;
}

int main() {
    string plaintext;
    string key;

    cout << "Enter the plaintext: ";
    getline(cin, plaintext);

    cout << "Enter the key (must be the same length as plaintext): ";
    getline(cin, key);

    // Check if the key is the same length as the plaintext
    if (key.length() != plaintext.length()) {
        cerr << "Error: The key must be the same length as the plaintext." << endl;
        return 1;
    }

    // Encrypt the plaintext
    string ciphertext = vernamEncrypt(plaintext, key);

    // Decrypt the ciphertext
    string decryptedText = vernamDecrypt(ciphertext, key);

    cout << "Plaintext: " << plaintext << endl;
    cout << "Key: " << key << endl;
    cout << "Ciphertext: " << ciphertext << endl;
    cout << "Decrypted Text: " << decryptedText << endl;

    return 0;
}
