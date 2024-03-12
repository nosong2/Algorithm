import sys
from collections import deque
input = sys.stdin.readline

di = [0, 1, 0, -1, 0, 0]
dj = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    for l in range(L):
        for i in range(R):
            for j in range(C):
                if building[l][i][j] == 'S':
                    SB_Start.append([l, i, j])
                    visited[l][i][j] = 1
    while SB_Start:
        z, y, x = SB_Start.popleft()
        for k in range(6):
            nz = z + dz[k]
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= nz < L and 0 <= ni < R and 0 <= nj < C and building[nz][ni][nj] != '#' and visited[nz][ni][nj] == 0:
                visited[nz][ni][nj] = visited[z][y][x] + 1
                if building[nz][ni][nj] == 'E':
                    print(f'Escaped in {visited[nz][ni][nj] - 1} minute(s).')
                    return
                SB_Start.append([nz, ni, nj])
    print('Trapped!')

while True:
    #L-높이 R-세로(행) C-가로(열)
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    check = deque()
    building = deque()
    SB_Start = deque()

    for _ in range(L):
        building.append([list(input()) for _ in range(R)])
        input()
    bfs()