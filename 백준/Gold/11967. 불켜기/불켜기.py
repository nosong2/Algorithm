import sys
from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

light = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
switch = [[[] for _ in range(N)] for _ in range(N)]
light[0][0] = 1
visited[0][0] = 1

for i in range(M):
    x, y, nx, ny = map(int, input().split())
    switch[x - 1][y - 1].append((nx - 1, ny - 1))


queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    if switch[x][y]:
        for r, g in switch[x][y]:
            if not light[r][g]:
                light[r][g] = 1
                for k in range(4):
                    nx = r + dx[k]
                    ny = g + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[x][y] = 1
                        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and light[nx][ny] and not visited[nx][ny]:
            queue.append((nx, ny))
            visited[nx][ny] = 1

print(sum(row.count(True) for row in light))
