import sys
input = sys.stdin.readline
from collections import deque

def left(level, direct):
    if level < 0:
        return
    if Gear[level][2] != Gear[level + 1][6]:
        left(level - 1, -direct)
        Gear[level].rotate(direct)

def right(level, direct):
    if level > 3:
        return
    if Gear[level][6] != Gear[level - 1][2]:
        right(level + 1, -direct)
        Gear[level].rotate(direct)


Gear = [deque(input().strip()) for _ in range(4)]
K = int(input())
result = 0
for k in range(K):
    subGear = Gear[:]
    who, direct = map(int, input().split())
    level = who - 1
    left(level - 1, -direct)
    right(level + 1, -direct)
    Gear[level].rotate(direct)

for i in range(4):
    if Gear[i][0] == '1':
        result += 2**i
print(result)