#include <stdio.h>

int main() {
  long long a, b, temp;
  int cnt = 0;

  scanf("%lld %lld", &a, &b);

  if (a > b) {
    temp = a;
    a = b;
    b = temp;
  }

  if (a == b) {
    printf("0");
  }
  else {
    printf("%lld\n", b - a - 1);
  }

  while (b - 1 > a) {
    a++;
    printf("%lld ", a);
  }

  return 0;
}