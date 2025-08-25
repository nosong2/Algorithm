import sys
from collections import deque

input = sys.stdin.readline

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]


L = (K + 1) * 2
def VIDX(y, x, b, t):
    return ((((y * M) + x) * (K + 1)) + b) * 2 + t

visited = bytearray(N * M * L)

q = deque()
q.append((0, 0, K, 1, 1))  
visited[VIDX(0, 0, K, 1)] = 1

while q:
    y, x, b, t, dist = q.popleft()
    if y == N - 1 and x == M - 1:
        print(dist)
        sys.exit(0)

    nt = t ^ 1 
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < M:
            if grid[ny][nx] == '0':
                vid = VIDX(ny, nx, b, nt)
                if not visited[vid]:
                    visited[vid] = 1
                    q.append((ny, nx, b, nt, dist + 1))
            else:
                if b > 0 and t == 1:
                    vid = VIDX(ny, nx, b - 1, nt)
                    if not visited[vid]:
                        visited[vid] = 1
                        q.append((ny, nx, b - 1, nt, dist + 1))
                elif b > 0 and t == 0:
                    vid = VIDX(y, x, b, nt)
                    if not visited[vid]:
                        visited[vid] = 1
                        q.append((y, x, b, nt, dist + 1))


print(-1)
