#include <stdio.h>

int main() {
  int a, b, c;
  int arr[10] = { 0 };
  int ain = 1;
  scanf("%d %d %d", &a, &b, &c);
  int value = a * b * c;
  while (value > 0) {
    arr[value % 10]++;
    value /= 10;
  }

  for (int i = 0; i < 10; i++) {
    printf("%d\n", arr[i]);
  }


  return 0;
}