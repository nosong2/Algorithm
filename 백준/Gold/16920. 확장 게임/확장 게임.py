import sys
from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, P = map(int, input().split())
S = list(map(int,input().split()))
visited = [[0] * M for _ in range(N)]
numcount = [0] * 10

mymap = [list(input().strip()) for _ in range(N)]

players = [deque() for _ in range(P + 1)]

for j in range(N):
    for i in range(M):
        ch = mymap[j][i]
        if '1' <= ch <= '9':
            p = ord(ch) - ord('0')
            visited[j][i] = p
            numcount[p] += 1
            players[p].append((j, i))

while True:
    progressed = False
    for a in range(P):
        p = a + 1
        step = S[a]
        for i in range(step):
            size = len(players[p])
            if size == 0:
                break
            for _ in range(size):

                y, x = players[a + 1].popleft()
                if visited[y][x] == 0: visited[y][x] = a + 1; numcount[p] += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N:
                        if visited[ny][nx] == 0 and mymap[ny][nx] == '.':
                            visited[ny][nx] = p
                            numcount[p] += 1
                            players[p].append((ny, nx))
                            progressed = True
    if not progressed:
        break
print(*numcount[1:P + 1])

