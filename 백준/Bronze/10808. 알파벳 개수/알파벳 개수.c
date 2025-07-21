#include <stdio.h>

int main() {
  char a[101];
  int alp[26] = {0};

  scanf("%s", &a);

  for (int i = 0; a[i] != '\0'; i++) {
    alp[a[i] - 'a']++;
  }
  for (int i = 0; i < 26; i++) {
    printf("%d ", alp[i]);
  }


  return 0;
}
