import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
Quere = deque()

def bfs():
    global cleanup
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                Quere.append([i, j])
                visited[i][j] = 1
                cleanup += 1
                while Quere:
                    x, y = Quere.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and abs(room[nx][ny] - room[x][y]) <= high:
                            visited[nx][ny] = 1
                            Quere.append([nx, ny])

n, m, high = map(int, input().split())

room = [list(map(int, input().split())) for i in range(n)]
visited = [[0] * m for _ in range(n)]
cleanup = 0

bfs()

print(cleanup)