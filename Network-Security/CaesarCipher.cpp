#include <iostream>
#include <string>

using namespace std;

string Encrypt(const string &text, int shift)
{
    string result = "";

    for (char ch : text)
    {
        if (isupper(ch))
        {
            result += char(int(ch - 'A' + shift) % 26 + 'A');
        }
        else if (islower(ch))
        {
            result += char(int(ch - 'a' + shift) % 26 + 'a');
        }
        else
        {
            result += ch; // Non-alphabetical characters remain unchanged
        }
    }
    return result;
}

string Decrypt(const string &text, int shift)
{
    string result = "";

    for (char ch : text)
    {
        if (isupper(ch))
        {
            result += char(int(ch - 'A' - shift + 26) % 26 + 'A');
        }
        else if (islower(ch))
        {
            result += char(int(ch - 'a' - shift + 26) % 26 + 'a');
        }
        else
        {
            result += ch; // Non-alphabetical characters remain unchanged
        }
    }
    return result;
}

int main()
{
    string text;
    int shift;

    cout << "Enter the Plain Text : ";
    getline(cin, text);

    cout << "Enter the Shift value : ";
    cin >> shift;

    string encryptedText = Encrypt(text, shift);
    string decryptedText = Decrypt(encryptedText, shift);

    cout << "Plain Text : " << text << endl;
    cout << "Encrypted Text : " << encryptedText << endl;
    cout << "Decrypted Text : " << decryptedText << endl;
}
