import sys
input = sys.stdin.readline

def dtd(level, Start):
    if level == M:
        print(*path)
        return
    for i in range(Start, N):
        if visited[i] == 1: continue
        visited[i] = 1
        path.append(i + 1)
        dtd(level + 1, i + 1)
        path.pop()
        visited[i] = 0



N, M = map(int, input().split())
visited = [0] * N
path = []

dtd(0, 0)