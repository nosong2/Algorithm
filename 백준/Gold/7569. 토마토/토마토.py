import sys
from collections import deque

def bfs():
    global count
    Queue = deque()
    for l in range(H):
        for i in range(N):
            for j in range(M):
                if arr[l][i][j] == 1:
                    Queue.append([l, i, j, count])
                    visited[l][i][j] = 1
    while Queue:
        z, x, y, count = Queue.popleft()
        count_list.append(count)
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and visited[nz][nx][ny] == 0 and arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = 1
                visited[nz][nx][ny] = 1
                Queue.append([nz, nx, ny, count + 1])


dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, sys.stdin.readline().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
count_list = []
count = 1
result = 0

bfs()

for l in arr:
    for i in l:
        for j in i:
            if j == 0:
                result = -1
if result != -1:
    result = max(count_list) - 1
print(result)
