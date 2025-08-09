import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
Quere = deque()

def bfs():
    global cleanup, oh, maxoh
    for i in range(n):
        for j in range(m):
            if room[i][j] == 1 and visited[i][j] == 0:
                Quere.append([i, j])
                visited[i][j] = 1
                cleanup += 1
                oh = 1
                while Quere:
                    x, y = Quere.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and room[nx][ny] == 1:
                            visited[nx][ny] = 1
                            Quere.append([nx, ny])
                            oh += 1
                if maxoh < oh: maxoh = oh

n, m = map(int, input().split())

room = [list(map(int, input().split())) for i in range(n)]
visited = [[0] * m for _ in range(n)]
cleanup = 0
oh = 0
maxoh = 0

bfs()

print(cleanup)
print(maxoh)