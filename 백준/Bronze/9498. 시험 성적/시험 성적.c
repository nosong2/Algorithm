#include <stdio.h>

int main() {

  int age;

  scanf("%d", &age);
  if (age >= 90) {
    //printf("%d\n", age);
    printf("A");
  }
  else if (age >= 80) {
    printf("B");
  }
  else if (age >= 70) {
    printf("C");
  }
  else if (age >= 60) {
    printf("D");
  }
  else {
    printf("F");
  }

  return 0;
}