import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
Quere = deque()

def bfs():
    global date
    for i in range(m):
        for j in range(n):
            if square[i][j] == 1:
                Quere.append([i, j, date])
                visited[i][j] = 1
    while Quere:
        x, y, date = Quere.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and square[nx][ny] == 0:
                square[nx][ny] = 1
                visited[nx][ny] = 1
                Quere.append([nx, ny, date + 1])


n, m = map(int, input().split())

square = [list(map(int, input().split())) for i in range(m)]
visited = [[0] * n for _ in range(m)]
date = 0
bfs()

for i in range(m):
    for j in range(n):
        if square[i][j] == 0:
            print(-1)
            exit(0)
print(date)