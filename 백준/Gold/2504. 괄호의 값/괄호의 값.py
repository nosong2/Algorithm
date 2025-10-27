import sys
from collections import deque

t = deque(input())
stack = deque()
result = 0
temp = 1

for i in range(len(t)):
    if t[i] == '(':
        temp *= 2
        stack.append(t[i])
    elif t[i] == '[':
        temp *= 3
        stack.append(t[i])
    elif t[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if t[i - 1] == '(':
            result += temp
        stack.pop()
        temp //= 2
    elif t[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if t[i - 1] == '[':
            result += temp
        stack.pop()
        temp //= 3
if stack:
    result = 0
print(result)

