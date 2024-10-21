//Hashing

#include <iostream>
#include <string>

using namespace std;

unsigned int RSHash(const string& str) {
    unsigned int a = 63689, b = 378551, hash = 0;
    for (char c : str) {
        hash = hash * a + c;
        a *= b;
    }
    return hash;
}

unsigned int JSHash(const string& str) {
    unsigned int hash = 1315423911;
    for (char c : str)
        hash ^= (hash << 5) + c + (hash >> 2);
    return hash;
}

unsigned int BKDRHash(const string& str) {
    unsigned int seed = 131, hash = 0;
    for (char c : str)
        hash = hash * seed + c;
    return hash;
}

unsigned int SDBMHash(const string& str) {
    unsigned int hash = 0;
    for (char c : str)
        hash = c + (hash << 6) + (hash << 16) - hash;
    return hash;
}

unsigned int DJBHash(const string& str) {
    unsigned int hash = 5381;
    for (char c : str)
        hash = ((hash << 5) + hash) + c;
    return hash;
}

int main() {
    string input;
    cout << "Enter a string to hash: ";
    getline(cin, input);
    
    cout << "RSHash: " << RSHash(input) << endl;
    cout << "JSHash: " << JSHash(input) << endl;
    cout << "BKDRHash: " << BKDRHash(input) << endl;
    cout << "SDBMHash: " << SDBMHash(input) << endl;
    cout << "DJBHash: " << DJBHash(input) << endl;

    return 0;
}
