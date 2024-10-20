#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

char calculateLRC(const vector<string> &data)
{
  char lrc = 0;
  for (const string &byte : data)
  {
    lrc ^= stoi(byte, nullptr, 2);
  }
  return lrc;
}

int main()
{
  vector<string> data = {"11100111", "11011101", "00111001", "10101001"};
  char lrc = calculateLRC(data);

  cout << "LRC : " << bitset<8>(lrc) << endl;
}