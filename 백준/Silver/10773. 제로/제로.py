import sys
from collections import deque

t = int(input())
stack = []

for _ in range(t):
    num = int(input())
    if num != 0: stack.append(num)
    else: stack.pop()
print(sum(stack))