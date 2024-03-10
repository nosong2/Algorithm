import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    global count
    while kimchi_list:
        i, j = kimchi_list.popleft()
        if visited[i][j] == 0:
            Queue.append([i, j])
            visited[i][j] = 1
            count += 1
            while Queue:
                y, x = Queue.popleft()
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 1 and visited[ni][nj] == 0:
                        Queue.append([ni, nj])
                        visited[ni][nj] = visited[y][x] + 1


T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    kimchi_list = deque()
    Queue = deque()
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        kimchi_list.append([x, y])
        field[x][y] = 1
    bfs()
    print(count)