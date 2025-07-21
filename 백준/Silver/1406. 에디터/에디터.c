#include <stdio.h>
#include <string.h> 
#define MAX 600001

char leftmax[MAX], rightmax[MAX];
int nowl = 0, nowr = 0;

int main() {

  char whereigoing;
  int t;

  scanf("%s", &leftmax);
  scanf("%d", &t);

  nowl = strlen(leftmax);
  for (int i = 0; i < t; i++) {
    scanf(" %c", &whereigoing);

    if (whereigoing == 'L') {
      if (nowl > 0) {
        rightmax[nowr++] = leftmax[--nowl];
      }
    }
    else if (whereigoing == 'D') {
      if (nowr > 0) {
        leftmax[nowl++] = rightmax[--nowr];
      }
    }
    else if (whereigoing == 'B') {
      if (nowl > 0) {
        --nowl;
      }

    } else if (whereigoing == 'P') {
      char word;
      scanf(" %c", &word);
      leftmax[nowl++] = word;
    }
  }

  for (int i = 0; i < nowl; i++) {
    printf("%c", leftmax[i]);
  }
  for (int i = nowr - 1; i >= 0; i--) {
    printf("%c", rightmax[i]);
  }

  return 0;
}
