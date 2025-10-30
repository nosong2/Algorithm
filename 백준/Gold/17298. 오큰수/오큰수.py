import sys

t = int(input())
arr = list(map(int, input().split()))
stack = []
result = [-1] * t

stack.append(0)
for i in range(1, t):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)