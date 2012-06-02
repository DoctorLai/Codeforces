#include <stdio.h>
#include <math.h>

int main()
{
  int n, i, k, r, x, found = 0;
  scanf("%d", &n);
  n *= 2;
  k = (sqrt(n * 1.0f) + 0.5f);
  for (i = 1; i < k; i ++)
  {
    r = n - i * i - i;
    x = (int)sqrt(r * 1.0f);
    if (x * (x + 1) == r)
    {
      found = 1;
      break;
    }
  } 
  if (found)
  {
    printf("YES");
  }
  else
  {
    printf("NO");
  }
  return (0);
}