#include <stdio.h>

int main() {
  int input[5];
  int data_size;
  int slot= 0;
  int sum = 0;

  for (int i = 0; i < 5; i++) {
    scanf("%d", &input[i]);
    sum += input[i];
  }

  data_size = sizeof(input) / sizeof(int);

  for (int i = 0; i < data_size; i++) {
    for (int j = 0; j < data_size - 1; j++) {
      if (input[j] > input[j + 1]) {
      slot = input[j];
      input[j] = input[j + 1];
      input[j + 1] = slot;
      }
    }
  }
  printf("%d\n%d", sum/data_size, input[2]);


  return 0;
}