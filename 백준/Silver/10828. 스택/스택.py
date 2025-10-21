import sys
from collections import deque

t = int(input())
result = []

for _ in range(t):
    who = input().split()
    if who[0] == "push":
        result.append(int(who[1]))
    elif who[0] == "pop":
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif who[0] == "size":
        print(len(result))
    elif who[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif who[0] == "top":
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])

