import sys
input = sys.stdin.readline
from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def down():
    while bbuu_list:
        y, x, color = bbuu_list.pop()
        for k in range(1):
            ni = y + di[k]
            if ni < N and bbuu[ni][x] == '.' and bbuu[y][x] != '.':
                # 자리 바꿈
                bbuu[ni][x], bbuu[y][x] = color, '.'
                bbuu_list.append([ni, x, color])


def bfs(i, j, c):
    global cnt, flag, result
    boom_list = []
    cnt = 0
    Queue.append([i, j, c])
    boom_list.append([i, j])
    while Queue:
        y, x, color = Queue.popleft()
        if visited[y][x] == 0:
            cnt += 1
        visited[y][x] = 1
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and bbuu[ni][nj] == color:
                visited[ni][nj] = 1
                cnt += 1
                Queue.append([ni, nj, color])
                boom_list.append([ni, nj])
    if cnt >= 4:
        flag = True
        for i in boom_list:
            bbuu[i[0]][i[1]] = '.'


N = 12
M = 6
bbuu = [list(input().strip()) for _ in range(N)]
bbuu_list = []
Queue = deque()
cnt = 0
result = 0

while True:
    flag = False
    visited = [[0] * M for _ in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if bbuu[i][j] != '.':
                bfs(i, j, bbuu[i][j])
        for j in range(M - 1, -1, -1):
            if bbuu[i][j] != '.' :
                bbuu_list.append([i, j, bbuu[i][j]])
                if len(bbuu_list) != 0:
                    down()
    if flag == True:
        result += 1
    else:
        break
print(result)

