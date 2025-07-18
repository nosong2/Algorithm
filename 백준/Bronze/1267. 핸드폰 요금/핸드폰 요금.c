#include <stdio.h>

int main() {
  int t;
  int ysum = 0, msum = 0;
  scanf("%d", &t);
  int arr[t];

  for (int i = 0; i < t; i++) {
    scanf("%d", &arr[i]);
    ysum += arr[i]/30 + 1;
    msum += arr[i]/60 + 1;
  }
  if (ysum * 10 < msum * 15) {
      printf("%s ", "Y");
      printf("%d", ysum * 10);
  } else if (msum * 15 < ysum * 10) {
      printf("%s ", "M");
      printf("%d", msum * 15);
  } else {
      printf("%s ", "Y M");
      printf("%d", ysum * 10);
  }

  return 0;
}