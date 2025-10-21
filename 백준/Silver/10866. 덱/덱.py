import sys
from collections import deque

t = int(input())
result = deque()

for _ in range(t):
    who = input().split()
    if who[0] == "push_front":
        result.appendleft(int(who[1]))
    elif who[0] == "push_back":
        result.append(int(who[1]))
    elif who[0] == "pop_front":
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    elif who[0] == "pop_back":
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
    elif who[0] == "back":
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
    elif who[0] == "front":
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])

