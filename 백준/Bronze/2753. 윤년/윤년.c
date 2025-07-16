#include <stdio.h>

int main() {
  int year;
  int answer = 0;

  scanf("%d", &year);

  if (year % 4 == 0 && year % 100 != 0) {
    answer = 1;
  }
  else if (year % 400 == 0) {
    answer = 1;
  }

  printf("%d", answer);

  return 0;
}