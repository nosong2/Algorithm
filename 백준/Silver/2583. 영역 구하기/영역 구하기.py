import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    global count
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 0:
                paper_list.append([i, j])
    while paper_list:
        q, w = paper_list.popleft()
        if visited[q][w] == 0:
            Queue.append([q, w])
            visited[q][w] = 1
            count = 0
            while Queue:
                count += 1
                y, x = Queue.popleft()
                if visited[y][x] == 0:
                    visited[y][x] = 1
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and paper[ni][nj] == 0:
                        visited[ni][nj] = visited[y][x] + 1
                        Queue.append([ni, nj])
            result.append(count)





M, N, K = map(int, input().split())
paper = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
paper_list = deque()
Queue = deque()
result = []
count = 0

for _ in range(K):
    x, y, X, Y = map(int, input().split())
    for i in range(x, X):
        for j in range(y, Y):
            paper[i][j] += 1
bfs()
result.sort()
print(len(result))
for i in result:
    print(i)