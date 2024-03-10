import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    global picture_size_save, picture_count
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1 and visited[i][j] == 0:
                paper_list.append([i, j])
    while paper_list:
        q, w = paper_list.popleft()
        if visited[q][w] == 0:
            Queue.append([q, w])
            visited[q][w] = 1
            picture_count += 1
            picture_size = 1
            while Queue:
                y, x = Queue.popleft()
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < M and paper[ni][nj] == 1 and visited[ni][nj] == 0:
                        Queue.append([ni, nj])
                        visited[ni][nj] = visited[y][x] + 1
                        picture_size += 1
                if picture_size_save < picture_size:
                    picture_size_save = picture_size


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
Queue = deque()
paper_list = deque()
picture_count = 0
picture_size_save = 0

bfs()
print(picture_count)
print(picture_size_save)