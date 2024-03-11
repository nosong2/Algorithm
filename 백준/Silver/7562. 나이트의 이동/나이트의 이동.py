import sys
from collections import deque
input = sys.stdin.readline

di = [1, 2, 1, 2, -1, -2, -1, -2]
dj = [2, 1, -2, -1, -2, -1, 2, 1]


def bfs(i, j):
    if i == result_i and j == result_j:
        print(0)
        return
    Queue = deque()
    Queue.append([i, j])
    visited[i][j] = 1
    while Queue:
        y, x = Queue.popleft()
        for k in range(8):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < L and 0 <= nj < L and visited[ni][nj] == 0:
                if ni == result_i and nj == result_j:
                    visited[ni][nj] = visited[y][x]
                    print(visited[ni][nj])
                    return
                Queue.append([ni, nj])
                visited[ni][nj] = visited[y][x] + 1



T = int(input())
for t in range(T):
    L = int(input())
    i, j = map(int, input().split())
    result_i, result_j = map(int, input().split())
    visited = [[0] * (L + 1) for _ in range(L + 1)]
    bfs(i, j)