import sys
from collections import deque

leng, kan = map(int, input().split())
now = 1
arr = deque()
result = []
for i in range(1, leng + 1):
    arr.append(i)
while arr:
    yo = arr.popleft()
    if now == kan:
        result.append(yo)
        now = 1
    else:
        arr.append(yo)
        now += 1

print("<", end="")
for i in range(len(result)):
    if i + 1 == leng:
        print(result[i], end="")
    else:
        print(result[i], end=", ")
print(">", end="")
