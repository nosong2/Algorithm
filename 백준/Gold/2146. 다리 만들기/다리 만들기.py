import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global shorenum
    while shore:
        y, x = shore.pop()
        visited[y][x] = 1
        place[y][x] = shorenum
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if place[ny][nx] == 1 and visited[ny][nx] == 0:
                    place[ny][nx] = shorenum
                    visited[ny][nx] = 1
                    shore.append((ny, nx))
    shorenum += 1

def createbridge():
    global maxbridge
    while continent:
        y, x, makebridge, myshore = continent.popleft()
        place[y][x] = makebridge
        visited2[y][x][myshore] = 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and visited2[ny][nx][myshore] == 0:
                if place[ny][nx] > 0 and place[ny][nx] != myshore and maxbridge < makebridge:
                    maxbridge = max(maxbridge, makebridge)
                elif 0 >= place[ny][nx] > makebridge > maxbridge:
                    visited2[ny][nx][myshore] = 1
                    continent.append((ny, nx, makebridge - 1, myshore))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
place = [list(map(int, input().split())) for _ in range(N)]
take = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited2 = [[[0] * 4 for _ in range(N)] for _ in range(N)]
shore = deque()
continent = deque()
shorenum = 1
maxbridge = -1000000

for i in range(N):
    for j in range(N):
        if place[i][j] == 1 and visited[i][j] == 0:
            shore.append((i, j))
            bfs()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if place[i][j] != 0 and place[nx][ny] == 0 and take[nx][ny] == 0:
                    take[nx][ny] = 1
                    continent.append([nx, ny, -1, place[i][j]])
visited2 = [[[0] * shorenum for _ in range(N)] for _ in range(N)]

createbridge()
print(abs(maxbridge))

