import sys
from collections import deque

t = deque(input())
stack = deque()

result = 0

for i in range(len(t)):
    if t[i] == '(':stack.append(t[i])
    elif t[i] == ')':
        if t[i - 1] == '(':
            stack.pop()
            result += len(stack)
        elif t[i - 1] == ')':
            stack.pop()
            result += 1
print(result)