import sys

t = int(input())

result = 0

while t > 0:
    if t % 5 == 0:
        result += t // 5
        t %= 5

    if t != 0:
        t -= 3
        result += 1

if t != 0: print(-1)
else: print(result)