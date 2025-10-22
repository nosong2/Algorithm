import sys
from collections import deque

t = int(input())

for i in range(t):
    how = input()
    num = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if num == 0:
        arr = deque()
    result = True
    reverse = False

    for i in how:
        if i == "R":
            reverse = not reverse
        elif i == "D":
            if len(arr) != 0 and not reverse:
                arr.popleft()
            elif len(arr) != 0 and reverse:
                arr.pop()
            else:
                result = False
    if reverse:
        arr.reverse()
    if result: print("[" + ",".join(map(str, arr)) + "]")
    else: print("error")
