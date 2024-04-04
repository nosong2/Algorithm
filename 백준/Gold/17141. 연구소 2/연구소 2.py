import sys
input = sys.stdin.readline
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    global zero_cnt, result
    non_virus = zero_cnt
    viru = 0
    visited = [[0] * N for _ in range(N)]
    Queue = deque(path)
    while Queue:
        by, bx = Queue.popleft()
        if visited[by][bx] == 0: visited[by][bx] = 1
        for k in range(4):
            ni = by + di[k]
            nj = bx + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and (laboratory[ni][nj] == 0 or laboratory[ni][nj] == 2):
                visited[ni][nj] = visited[by][bx] + 1
                viru += 1
                Queue.append([ni, nj])
    if non_virus - (viru + M) == 0:
        result = min(result, visited[by][bx] - 1)
        return

def jo(level, Start):
    if level == M:
        bfs()
        return
    for q in range(Start, len(virus)):
        y, x = virus[q]
        laboratory[y][x] = 'V'
        path.append([y, x])
        jo(level + 1, q + 1)
        path.pop()
        laboratory[y][x] = 2





N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]
zero_cnt = 0
virus = []
path = deque()
result = 9999999999

for i in range(N):
    for j in range(N):
        if laboratory[i][j] == 0:
            zero_cnt += 1
        elif laboratory[i][j] == 2:
            virus.append([i, j])
            zero_cnt += 1
if M == 0:
    print(0)
    exit(0)

jo(0, 0)
if result == 9999999999:
    print(-1)
else:
    print(result)