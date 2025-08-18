import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def swimswan():
    swan_next = deque()
    while swanQ:
        my, mx = swanQ.popleft()
        visited[my][mx] = 1
        if (my, mx) == (ty, tx): return True
        for k in range(4):
            nx = my + dx[k]
            ny = mx + dy[k]
            if 0 <= nx < y and 0 <= ny < x and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if lake[nx][ny] == ".":
                    swanQ.append((nx, ny))
                else:
                    swan_next.append((nx, ny))
    return swan_next



def meltice():
    global day, nextdaymelt, qubox
    while qubox:
        my, mx = qubox.popleft()
        for k in range(4):
            nx = my + dx[k]
            ny = mx + dy[k]
            if 0 <= nx < y and 0 <= ny < x and lake[nx][ny] == "X":
                lake[nx][ny] = "."
                nextdaymelt.append((nx, ny))
    qubox, nextdaymelt = nextdaymelt, deque()
    day += 1


y, x = map(int, input().split())
lake = [list(input().strip()) for _ in range(y)]
qubox = deque()
swan = deque()
nextdaymelt = deque()
day = 0
visited = [[0] * x for _ in range(y)]

for i in range(y):
    for j in range(x):
        if lake[i][j] == "L": swan.append((i, j))
        if lake[i][j] == "." or lake[i][j] == "L": qubox.append((i, j))


(sy, sx), (ty, tx) = swan
swanQ = deque([(sy, sx)])
lake[sy][sx] = '.'
lake[ty][tx] = '.'

while True:
    a = swimswan()
    if a == 1:
        print(day)
        break
    swanQ = a
    meltice()
