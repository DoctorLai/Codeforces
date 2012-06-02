#include <iostream>
#include <math.h>

using namespace std;

int main()
{
  int n;
  cin >> n;
  n *= 2;
  int k = int(sqrt(n * 1.0f) + 0.5f);
  bool found = false;
  for (int i = 1; i < k; i ++)
  {
    int r = n - i * i - i;
    int x = (int)sqrt(r * 1.0f);
    if (x * (x + 1) == r)
    {
      found = true;
      break;
    }
  } 
  if (found)
  {
    cout << "YES";
  }
  else
  {
    cout << "NO";
  }
  return (0);
}