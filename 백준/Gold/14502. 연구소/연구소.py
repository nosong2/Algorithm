import sys
input = sys.stdin.readline
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    global result
    visited2 = [[0] * M for _ in range(N)]
    Queue = deque(virus)
    while Queue:
        y, x = Queue.popleft()
        visited2[y][x] = 2
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited2[ni][nj] == 0 and laboratory[ni][nj] == 0:
                visited2[ni][nj] = 2
                Queue.append([ni, nj])
    safe = 0
    for a in range(N):
        for s in range(M):
            if visited2[a][s] == 0 and laboratory[a][s] == 0:
                safe += 1
    result = max(safe, result)
    return


def dfs(level, wallcnt):
    if level == 3:
        bfs()
        return
    for i in range(len(z)):
        if visited[z[i][0]][z[i][1]] == 1: continue
        laboratory[z[i][0]][z[i][1]] = 1
        visited[z[i][0]][z[i][1]] = 1
        dfs(level + 1, wallcnt - 1)
        visited[z[i][0]][z[i][1]] = 0
        laboratory[z[i][0]][z[i][1]] = 0




N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]
wallcount = 3
visited = [[0] * M for _ in range(N)]
road = []
virus = []
z = []
cnt = 0
result = 0
gas = -9999999999

for i in range(N):
    for j in range(M):
        if laboratory[i][j] ==0:
            z.append([i, j])
        if laboratory[i][j] == 2:
            virus.append([i, j])
dfs(0, wallcount)
print(result)