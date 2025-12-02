import sys

t = int(input())

for i in range(t):
    a = int(input())
    arr = [0] * (a + 1)
    for j in range(1, a + 1):
        for k in range(1, a + 1):
            if j * k <= a:
                if arr[j * k] == 0:
                    arr[j * k] = 1
                else:
                    arr[j * k] = 0
    print(sum(arr))