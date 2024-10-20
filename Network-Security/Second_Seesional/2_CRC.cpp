#include <iostream>
#include <string>

using namespace std;

string xorOperation(string a, string b)
{
  string result = "";
  for (int i = 1; i < b.length(); i++)
  {
    result += (a[i] == b[i]) ? '0' : '1';
  }
  return result;
}

string calculateCRC(string data, string key)
{
  int keyLength = key.length();

  string appendData = data + string(keyLength - 1, '0');

  string remainder = appendData.substr(0, keyLength);

  for (int i = keyLength; i <= appendData.length(); i++)
  {
    if (remainder[0] == '1')
    {
      remainder = xorOperation(remainder, key);
    }
    else
    {
      remainder = xorOperation(remainder, string(keyLength, '0'));
    }

    if (i < appendData.length())
    {
      remainder += appendData[i];
    }
  }
  return remainder;
}

int main()
{
  string data = "1001";
  string key = "1011";

  string crc = calculateCRC(data, key);

  cout << "Data : " << data << endl;
  cout << "CRC : " << crc << endl;
  cout << "Final message with CRC : " << data << crc << endl;

  return 0;
}