#include <stdio.h>

int main() {
  int input[9];
  int data_size;
  int slot= 0;
  int sum = 0;

  for (int i = 0; i < 9; i++) {
    scanf("%d", &input[i]);
    sum += input[i];
  }

  data_size = sizeof(input) / sizeof(int);

  for (int i = 0; i < data_size; i++) {
    for (int j = 0; j < data_size - 1; j++) {
      if (input[i] != input[j] && sum - input[i] - input[j] == 100) {
        input[i] = 0;
        input[j] = 0;
        break;
      }
    }
    if (input[i] == 0) break;
  }

  for (int i = 0; i < data_size; i++) {
    for (int j = 0; j < data_size - 1; j++) {
      if (input[j] > input[j + 1]) {
        slot = input[j];
        input[j] = input[j + 1];
        input[j + 1] = slot;
      }
    }
  }

  for (int i = 0; i < data_size; i++) {
    if (input[i] != 0) {
      printf("%d\n", input[i]);
    }
  }

  return 0;
}