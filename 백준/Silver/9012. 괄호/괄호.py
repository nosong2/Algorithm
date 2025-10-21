import sys

t = int(input())

for _ in range(t):
    result = [0, 0]
    real = True
    n = input().strip()

    for i in n:
        if result[1] > result[0]:
            real = False
            break
        if i == "(":
            result[0] += 1
        elif i == ")":
            result[1] += 1
    if result[0] != result[1]:
        real = False
    if not real:
        print("NO")
    else:
        print("YES")
