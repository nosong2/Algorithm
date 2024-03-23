import sys
input = sys.stdin.readline

def dfs(y, x, pipe):
    global count
    if house[N - 1][N - 1] == 1 or (house[N - 1][N - 2] == 1 and house[N - 2][N - 1] == 1):
        print(0)
        exit(0) 
    if (x == N - 1 and y != N - 1 and pipe == 2) or (x != N - 1 and y == N - 1 and pipe == 3):
        return
    if y == x == (N - 1):
        count += 1
        return
    if pipe == 2: # 가로
        if x + 1 < N and house[y][x + 1] == 0:
            dfs(y, x + 1, pipe)
        if y + 1 < N and x + 1 < N and house[y][x + 1] == house[y + 1][x] == house[y + 1][x + 1] == 0:
            dfs(y + 1, x + 1, pipe + 2)

    if pipe == 3: # 세로
        if y + 1 < N and house[y + 1][x] == 0:
            dfs(y + 1, x, pipe)
        if y + 1 < N and x + 1 < N and house[y][x + 1] == house[y + 1][x] == house[y + 1][x + 1] == 0:
            dfs(y + 1, x + 1, pipe + 1)

    if pipe == 4: # 대각
        if x + 1 < N and house[y][x + 1] == 0:
            dfs(y, x + 1, pipe - 2)
        if y + 1 < N and house[y + 1][x] == 0:
            dfs(y + 1, x, pipe - 1)
        if y + 1 < N and x + 1 < N and house[y][x + 1] == house[y + 1][x] == house[y + 1][x + 1] == 0:
            dfs(y + 1, x + 1, pipe)


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
count = 0


dfs(0, 1, 2)
print(count)
