#include <stdio.h>

int main() {
  int a;
  int max = 0;
  int count = 0;

  for (int i = 0; i < 9; i++) {
    scanf("%d", &a);
    if (a > max) {
      max = a;
      count = i + 1;
    }
  }

  printf("%d\n%d", max, count);

  return 0;
}