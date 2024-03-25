import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
skill = list(map(int, input().split()))
card = deque()
skill.reverse()

for i in range(1, N + 1):
    if skill[i - 1] == 1:
        card.insert(0, i)
    elif skill[i - 1] == 2:
        card.insert(1, i)
    elif skill[i - 1] == 3:
        card.append(i)

print(*card)