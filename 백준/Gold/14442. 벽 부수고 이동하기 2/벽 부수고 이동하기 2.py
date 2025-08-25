import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
mymap = [list(map(int, input())) for _ in range(N)]
mystage = deque([(0, 0, K)])
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][K] = 1
while mystage:
    y, x, broken = mystage.popleft()
    if y == N - 1 and x == M - 1:
        print(visited[y][x][broken])
        exit(0)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < M and 0 <= ny < N:
            if mymap[ny][nx] == 0 and visited[ny][nx][broken] == 0:
                visited[ny][nx][broken] = visited[y][x][broken] + 1
                mystage.append((ny, nx, broken))
            elif mymap[ny][nx] == 1 and broken != 0 and visited[ny][nx][broken - 1] == 0:
                visited[ny][nx][broken - 1] = visited[y][x][broken] + 1
                mystage.append((ny, nx, broken - 1))
print(-1)
