import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    for i in range(M):
        for j in range(N):
            if box[i][j] == 1:
                Queue.append([i, j])
                visited[i][j] = 1
    while Queue:
        y, x = Queue.popleft()
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < M and 0 <= nj < N and box[ni][nj] == 0 and visited[ni][nj] == 0:
                box[ni][nj] = 1
                visited[ni][nj] = visited[y][x] + 1
                Queue.append([ni, nj])


N, M = map(int, (input().split()))
box = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
result = 0
Queue = deque()

bfs()
for i in range(M):
    for j in range(N):
        if box[i][j] == 0:
            result = -1
if max(sum(visited, [])) != 0 and result != -1:
    result = max(sum(visited, [])) - 1
print(result)