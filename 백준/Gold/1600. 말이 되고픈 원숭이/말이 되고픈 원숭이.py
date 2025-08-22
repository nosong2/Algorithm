import sys
from collections import deque


K = int(input())
N, M = map(int, input().split())
mymap = [list(map(int, input().split())) for _ in range(M)]
visited = [[[0] * (K + 1) for _ in range(N)] for _ in range(M)]
monkey = deque()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
horsedx = [2, 1, -2, -1, 2, 1, -2, -1]
horsedy = [1, 2, 1, 2, -1, -2, -1, -2]
monkey.append((0, 0, K))
visited[0][0][K] = 1
while monkey:
    y, x, horsejump = monkey.popleft()
    if y == M - 1 and x == N - 1:
        print(visited[y][x][horsejump] - 1)
        exit(0)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if mymap[ny][nx] == 0 and visited[ny][nx][horsejump] == 0:
                visited[ny][nx][horsejump] = visited[y][x][horsejump] + 1
                monkey.append((ny, nx, horsejump))
    if horsejump != 0:
        for h in range(8):
            hx = x + horsedx[h]
            hy = y + horsedy[h]
            if 0 <= hx < N and 0 <= hy < M:
                if mymap[hy][hx] == 0 and visited[hy][hx][horsejump - 1] == 0:
                    visited[hy][hx][horsejump - 1] = visited[y][x][horsejump] + 1
                    monkey.append((hy, hx, horsejump - 1))
print(-1)