import sys

t = int(input())
arr = list(map(int, input().split()))
checkpoint = int(input())
result = 0

arr.sort()

for i in range(t):
    for j in range(i + 1, t):
        if arr[i] + arr[j] == checkpoint:
            result += 1
        elif arr[i] + arr[j] > checkpoint: break
print(result)