import sys
from collections import deque

def countingpaper(x, y, size):
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                for a in range(2):
                    for b in range(2):
                        countingpaper(x + (size // 2) * a, y + (size // 2) * b, size // 2)
                return

    result.append(color)

t = int(input())
paper = [list(map(int, input().split())) for _ in range(t)]
result = []


countingpaper(0, 0, t)


print(result.count(0))
print(result.count(1))