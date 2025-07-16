#include <stdio.h>

int main() {
  int a;
  int sum = 0;
  int max = 101;

  for (int i = 0; i < 7; i++) {
    scanf("%d", &a);
    if (a % 2 != 0) {
      sum += a;
      if (a < max) {
        max = a;
      }
    }
  }

  if (sum == 0) {
      printf("-1");
  }
  else {
  printf("%d\n%d", sum, max);
  }
  return 0;
}