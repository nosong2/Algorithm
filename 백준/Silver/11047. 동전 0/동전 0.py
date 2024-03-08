import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
coin = deque()
count = 0

for _ in range(N):
    coin.append(int(input()))
while K != 0:
    x = coin.pop()
    while K - x >= 0:
        if K - x >= 0:
            K -= x
            count += 1
        elif K - x < 0:
            break
print(count)