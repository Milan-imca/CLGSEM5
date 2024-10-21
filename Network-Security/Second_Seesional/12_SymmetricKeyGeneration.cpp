//For Symmetric key generation

#include <iostream>
#include <openssl/rand.h>
#include <string>

using namespace std;

void generateSymmetricKey(int keyLength, const string& algorithmName) {
    unsigned char key[64];  // Max key size: 64 bytes
    if (keyLength > sizeof(key) || RAND_bytes(key, keyLength) != 1) {
        cout << "Error generating key." << endl;
        return;
    }
    cout << algorithmName << " Key: ";
    for (int i = 0; i < keyLength; i++) printf("%02X", key[i]);
    cout << endl;
}

int main() {
    string algorithmName;
    cout << "Enter algorithm (des/blowfish/idea/triple des): ";
    getline(cin,algorithmName);

    int keyLength = (algorithmName == "des") ? 8 :
                    (algorithmName == "blowfish" || algorithmName == "idea") ? 16 :
                    (algorithmName == "triple des") ? 24 : 0;

    if (keyLength == 0) {
        cout << "Invalid algorithm." << endl;
    } else {
        generateSymmetricKey(keyLength, algorithmName);
    }

    return 0;
}
