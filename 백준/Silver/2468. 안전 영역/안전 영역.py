import sys
sys.setrecursionlimit(10**7)
# N은 2 이상 100
# 높이는 1이상 100 이하의 정수이다.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(Sx, Sy):
    global count
    visited[Sx][Sy] = count
    for k in range(4):
        nx = Sx + dx[k]
        ny = Sy + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] != 0:
            dfs(nx, ny)
    count_list.append(count)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 1
count_list = []

for rain in range(0, 101):
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= rain:
                arr[i][j] = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:
                dfs(i, j)
                count += 1
    count = 1
    visited = [[0] * N for _ in range(N)]

print(max(count_list))