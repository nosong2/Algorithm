import sys

t = int(input())
stack = []
result = 0
for _ in range(t):
    if not stack:
        stack.append(int(input()))
    else:
        now = int(input())
        while stack:
            if stack[-1] > now:
                stack.append(now)
                result = result + (len(stack) - 1)
                break
            else:
                stack.pop()
                if not stack:
                    stack.append(now)
                    break
print(result)