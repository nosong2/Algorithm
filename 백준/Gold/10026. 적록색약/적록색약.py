import sys
input = sys.stdin.readline
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    global count
    while person:
        q, w, col = person.popleft()
        if visited[q][w] == 0:
            color_area.append([q, w, col])
            visited[q][w] = 1
            count += 1
        while color_area:
            y, x, col = color_area.popleft()
            if col == 'R':
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and color[ni][nj] == 'R':
                        visited[ni][nj] = visited[y][x] + 1
                        color_area.append([ni, nj, col])

            elif col == 'B':
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and color[ni][nj] =='B':
                        visited[ni][nj] = visited[y][x] + 1
                        color_area.append([ni, nj, col])

            elif col == 'G':
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and color[ni][nj] == 'G':
                        visited[ni][nj] = visited[y][x] + 1
                        color_area.append([ni, nj, col])

def cbfs():
    global count2
    while person2:
        q, w, col = person2.popleft()
        if visited2[q][w] == 0:
            color_area.append([q, w, col])
            visited2[q][w] = 1
            count2 += 1
        while color_area:
            y, x, col = color_area.popleft()
            if col == 'R':
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and visited2[ni][nj] == 0 and (color[ni][nj] == 'R' or color[ni][nj] == 'G'):
                        visited2[ni][nj] = visited2[y][x] + 1
                        color_area.append([ni, nj, col])

            if col == 'B':
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and visited2[ni][nj] == 0 and color[ni][nj] =='B':
                        visited2[ni][nj] = visited2[y][x] + 1
                        color_area.append([ni, nj, col])



N = int(input())
color = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
count = 0
count2 = 0
person = deque()
person2 = deque()
color_area = deque()

for i in range(N):
    for j in range(N):
        if color[i][j] == 'R':
            person.append([i, j, color[i][j]])
            person2.append([i, j, color[i][j]])
        elif color[i][j] == 'B':
            person.append([i, j, color[i][j]])
            person2.append([i, j, color[i][j]])
        elif color[i][j] == 'G':
            person.append([i, j, color[i][j]])
            person2.append([i, j, 'R'])


bfs()
cbfs()
print(count)
print(count2)