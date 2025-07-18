#include <stdio.h>

int main() {
  int t;
  scanf("%d", &t);

  for (int i = 2; i <= t; i++) {
    for (int k = t; k >= i; k--) {
      printf("%s", " ");
    }
    for (int q = 1; q < i; q++) {
      printf("%s", "*");
    }
    for (int w = 2; w < i; w++) {
      printf("%s", "*");
    }
    printf("\n");

  }


  for (int i = 1; i <= t; i++) {
    for (int k = 1; k < i; k++) {
      printf("%s", " ");
    }
    for (int j = t; j >= i; j--) {
      printf("%s", "*");
    }
    for (int l = t; l > i; l--) {
      printf("%s", "*");
    }
    printf("\n");
  }

  return 0;
}