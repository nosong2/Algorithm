#include <stdio.h>

int main() {
  int arr[20];
  int a, b;
  int slot;
  for (int i = 0; i < 20; i++) {
    arr[i]= i + 1;
  }
  for (int i = 0; i < 10; i++) {
    scanf("%d %d", &a, &b);

    for (int i = 0; i < (b - a) / 2 + 1; i++) {
      slot = arr[a + i - 1];
      arr[a + i - 1] = arr[b - i - 1];
      arr[b - i - 1] = slot;
    }
  }
  for (int i = 0; i < 20; i++) {
    printf("%d ", arr[i]);
  }
  return 0;
}