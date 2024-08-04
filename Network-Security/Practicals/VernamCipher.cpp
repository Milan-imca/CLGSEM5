#include <iostream>
#include <string>
#include <cctype>

using namespace std;

// Function to convert a character to its corresponding 0-25 value
int charToValue(char c) {
    if (isupper(c)) {
        return c - 'A';
    } else if (islower(c)) {
        return c - 'a';
    } else {
        // Handle other characters as needed (e.g., ignore, replace, or error)
        return -1; // Indicate invalid character
    }
}

// Function to convert a 0-25 value to its corresponding character
char valueToChar(int v, bool isUpper) {
    return isUpper ? 'A' + v : 'a' + v;
}

// Function to encrypt plaintext using Vernam cipher (one-time pad)
string vernamEncrypt(string plaintext, string key) {
    if (plaintext.length() != key.length()) {
        cerr << "Error: Plaintext and key lengths must be equal." << endl;
        return "";
    }

    string ciphertext = "";
    for (int i = 0; i < plaintext.length(); i++) {
        int pVal = charToValue(plaintext[i]);
        int kVal = charToValue(key[i]);
        if (pVal == -1 || kVal == -1) {
            // Handle invalid characters (e.g., ignore, replace, or error)
            ciphertext += plaintext[i]; // Keep original character
        } else {
            bool isUpper = isupper(plaintext[i]);
            int cVal = (pVal + kVal) % 26;
            ciphertext += valueToChar(cVal, isUpper);
        }
    }
    return ciphertext;
}

// Function to decrypt ciphertext using Vernam cipher (one-time pad)
string vernamDecrypt(string ciphertext, string key) {
    if (ciphertext.length() != key.length()) {
        cerr << "Error: Ciphertext and key lengths must be equal." << endl;
        return "";
    }

    string plaintext = "";
    for (int i = 0; i < ciphertext.length(); i++) {
        int cVal = charToValue(ciphertext[i]);
        int kVal = charToValue(key[i]);
        if (cVal == -1 || kVal == -1) {
            // Handle invalid characters (e.g., ignore, replace, or error)
            plaintext += ciphertext[i]; // Keep original character
        } else {
            bool isUpper = isupper(ciphertext[i]);
            int pVal = (cVal - kVal + 26) % 26;
            plaintext += valueToChar(pVal, isUpper);
        }
    }
    return plaintext;
}

int main() {
    string plaintext = "attack ATTACK";
    string key = "czvcbo CZVCBO";

    string ciphertext = vernamEncrypt(plaintext, key);
    cout << "Ciphertext: " << ciphertext << endl;

    string decryptedText = vernamDecrypt(ciphertext, key);
    cout << "Decrypted Text: " << decryptedText << endl;

    return 0;
}
