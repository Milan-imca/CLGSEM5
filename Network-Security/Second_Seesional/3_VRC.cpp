#include<iostream>
#include<bitset>

using namespace std;

char calculateVRC(string byte,bool isEvenparity){
  int parity = 0;
  for (char bit:byte){
    if(bit == 1){
      parity++;
    }
  }

  if (isEvenparity){
    return (parity % 2 == 0) ? '0' : '1';
  }
  else{
    return (parity % 2 == 0) ? '1' : '0';
  }
}


int main(){
  string data;
  int parityChoice;
  
  cout<<"Enter the data(binary String) : ";
  cin>>data;

  cout<<"Choose parity type : \n0 : Even\n1: Odd\n";
  cin>>parityChoice;

  bool isEvenParity = (parityChoice == 0);

  char vrc = calculateVRC(data,isEvenParity);

  cout << "VRC (" << (isEvenParity ? "even" : "odd") << " parity) for " << data << " : " << vrc << endl;
  cout << "Final data with VRC " << data << vrc <<endl;

}

