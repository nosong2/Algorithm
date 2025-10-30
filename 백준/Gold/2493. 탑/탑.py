import sys

t = int(input())
arr = list(map(int, input().split()))
stack = []
result = [0] * t

stack.append(t - 1)
for i in range(t - 2, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = i + 1
    stack.append(i)
print(*result)