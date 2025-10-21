import sys
from collections import deque

t = int(input())
stack = []
result = []
ucan = True
now = 1

for _ in range(t):
    num = int(input())
    while num >= now:
        stack.append(now)
        result.append("+")
        now += 1
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        ucan = False

if not ucan:
    print("NO")
else:
    for i in result:
        print(i)
