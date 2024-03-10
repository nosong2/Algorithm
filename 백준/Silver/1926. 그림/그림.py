import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def find_picture():
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1 and visited[i][j] == 0:
                paper_list.append([i, j])

def dfs(i, j):
    global picture_size, picture_size_save, picture_count
    if visited[i][j] != 0:
        picture_count -= 1
        return
    picture_count += 1
    if picture_size_save < picture_size:
        picture_size_save = picture_size
    visited[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and paper[ni][nj] == 1 and visited[ni][nj] == 0:
            picture_size += 1
            dfs(ni, nj)


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
paper_list = deque()
picture_count = 0
picture_size_save = 0
find_picture()
while paper_list:
    picture_size = 1
    y, x = paper_list.popleft()
    dfs(y, x)
print(picture_count)
print(picture_size_save)