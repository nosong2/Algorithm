import sys

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
result = {}
for i in Nlist:
    result[i] = 1
for i in Mlist:
    if i in result:
        print(result[i], end=" ")
    else:
        print(0, end=" ")
