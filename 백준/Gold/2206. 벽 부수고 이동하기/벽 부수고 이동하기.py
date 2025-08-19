import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


y, x = map(int, input().split())
place = [list(map(int, input().strip())) for _ in range(y)]
visited = [[[0] * 2 for _ in range(x)] for _ in range(y)]
visited[0][0][0] = 1
mystart = deque([(0, 0, 0)])

while mystart:
    my, mx, breakwall = mystart.popleft()
    if my == y - 1 and mx == x - 1:
        print(visited[my][mx][breakwall])
        exit(0)
    for k in range(4):
        nx = mx + dx[k]
        ny = my + dy[k]
        if 0 <= nx < x and 0 <= ny < y and visited[ny][nx][breakwall] == 0 and place[ny][nx] == 0:
            visited[ny][nx][breakwall] = visited[my][mx][breakwall] + 1
            mystart.append((ny, nx, breakwall))
        elif 0 <= nx < x and 0 <= ny < y and visited[ny][nx][breakwall] == 0 and place[ny][nx] == 1 and breakwall == 0:
            visited[ny][nx][1] = visited[my][mx][breakwall] + 1
            mystart.append((ny, nx, 1))
print(-1)


