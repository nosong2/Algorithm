import sys
from collections import deque

subin, bro = map(int, input().split())

time = [0] * 500001
temp = [[0] * 2 for _ in range(500001)]
def bfs():
    queue = deque()
    queue.append([subin, 0])
    while queue:
        x, times = queue.popleft()
        bros = bro + times * (times + 1) // 2
        if bros >= 500001:
            print(-1)
            break
        if temp[bros][times % 2]:
            print(times)
            return
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 500000 and not temp[i][(times+1)%2]:
                queue.append((i, times + 1))
                temp[i][(times+1)%2] = 1
if subin == bro:print(0)
else: bfs()
