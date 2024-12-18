// Stop and wait program

#include <iostream>
#include <cstdlib> // For rand()
#include <ctime>   // For time()

using namespace std;

class StopAndWait
{
  public:
    void sendData(int frames)
    {
      for (int i = 1; i <= frames; i++)
      {
        cout << "Sending frame " << i << endl;
        if (!receiveAck())
        {
          cout << "Ack not received. Resending frame " << i << endl;
          i--; // Resend the same frame
        }
      }
      cout << "All frames sent successfully!" << endl;
    }

  private:
    bool receiveAck() { return rand() % 2; } // Randomly simulate ack/no-ack
};

int main()
{
  srand(time(0)); // Seed random number generator
  int frames;
  cout << "Enter number of frames: ";
  cin >> frames;

  StopAndWait().sendData(frames);
  return 0;
}
