import sys
from collections import deque

# input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def whereisJHandfire():
    for i in range(C):
        for j in range(R):
            if maze[i][j] == 'F':
                Fire_list.append([i, j, 'F'])
            elif maze[i][j] == 'J':
                JH_list.append([i, j, 'J'])
    q, w, e = JH_list.popleft()
    JH_visited[q][w] = 1
    Fire_list.append([q, w, e])
    while Fire_list:
        y, x, who = Fire_list.popleft()
        if who == 'J':
            if (y == 0 or y == C - 1) or (x == 0 or x == R - 1):
                print(JH_visited[y][x])
                return
            for k in range(4):
                ni = y + di[k]
                nj = x + dj[k]
                if 0 <= ni < C and 0 <= nj < R and maze[ni][nj] != '#' and maze[ni][nj] != 'F' and JH_visited[ni][nj] == 0:
                    JH_visited[ni][nj] = JH_visited[y][x] + 1
                    if (ni == 0 or ni == C - 1) or (nj == 0 or nj == R - 1):
                        print(JH_visited[ni][nj])
                        return
                    maze[ni][nj] = 'J'
                    Fire_list.append([ni, nj, 'J'])
        else:
            for k in range(4):
                ni = y + di[k]
                nj = x + dj[k]
                if 0 <= ni < C and 0 <= nj < R and maze[ni][nj] != '#' and maze[ni][nj] != 'F':
                    maze[ni][nj] = 'F'
                    Fire_list.append([ni, nj, 'F'])
    print('IMPOSSIBLE')

C, R = map(int, input().split())
maze = [list(input()) for _ in range(C)]
JH_visited = [[0] * R for _ in range(C)]
JH_list = deque()
Fire_list = deque()

whereisJHandfire()
