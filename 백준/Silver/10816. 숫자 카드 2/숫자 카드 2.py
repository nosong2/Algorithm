import sys

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
# result = [0] * 20000000
result = {}
for i in Nlist:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
for i in Mlist:
    if i in result:
        print(result[i], end=" ")
    else:
        print(0, end=" ")
