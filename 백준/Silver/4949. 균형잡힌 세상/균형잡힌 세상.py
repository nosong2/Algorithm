import sys

# 입력을 빠르게 받기 위해 sys.stdin 사용
input = sys.stdin.readline

result = []

while True:
    line = input().rstrip()
    if line == ".":
        break

    stack = []
    balanced = True

    for char in line:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balanced = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balanced = False
                break

    if balanced and not stack:
        result.append("yes")
    else:
        result.append("no")

for r in result:
    print(r)
