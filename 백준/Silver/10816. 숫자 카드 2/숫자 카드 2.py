import sys

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
result = [0] * 20000001

for i in Nlist:
    result[i] += 1
for i in Mlist:
    print(result[i], end=" ")
