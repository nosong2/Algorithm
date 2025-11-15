import sys
from collections import deque

t = int(input())

def hanoi(num, from_, to, other):
    if num == 0:
        return
    hanoi(num - 1, from_, other, to)
    print(from_, to)
    hanoi(num - 1, other, to, from_)

print(2**t - 1)
hanoi(t, 1, 3, 2)