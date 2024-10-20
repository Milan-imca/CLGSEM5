#include <iostream>
using namespace std;

class SlidingWindow
{
public:
  SlidingWindow(int ws, int tf) : windowSize(ws), totalFrames(tf) {}

  void sendFrames()
  {
    for (int i = 0; i < totalFrames; i++)
    {
      int end = min(i + windowSize, totalFrames);
      cout << "\nSending frames " << i + 1 << " to " << end << endl;
      cout << "Acknowledgment received for frame " << i + 1 << endl;
    }
    cout << "All frames sent and acknowledged successfully!" << endl;
  }

private:
  int windowSize, totalFrames;
};

int main()
{
  int windowSize, totalFrames;
  cout << "Enter window size and total frames: ";
  cin >> windowSize >> totalFrames;

  SlidingWindow protocol(windowSize, totalFrames);
  protocol.sendFrames();
  return 0;
}
