import sys
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def find_sea():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                sea_box.append([i, j])


def melt_ice():
    global count, result
    result += 1
    for _ in range(len(sea_box)):
        y, x = sea_box.popleft()
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0: continue
                arr[ni][nj] -= 1
                if arr[ni][nj] == 0:
                    sea_box.append([ni, nj])
                count += 1
        if count >= 1:
            sea_box.append([y, x])
            count = 0


def bfs():
    global flag
    y, x = -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                y, x = i, j
                if y > 0 and x > 0:
                    break
        if y > 0 and x > 0:
            break
    Queue = deque()
    Queue.append([y, x])
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    while Queue:
        y, x = Queue.popleft()
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] > 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                Queue.append([ni, nj])
    for q in range(N):
        for w in range(M):

            if arr[q][w] != 0 and visited[q][w] == 0:
                flag = 1
                return


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sea_box = deque()
flag = 0
count = 0
result = 0

find_sea()
while sum(sum(arr,[])) != 0:
    melt_ice()
    bfs()
    if flag == 1:
        print(result)
        break
if sum(sum(arr,[])) == 0:
    print(0)