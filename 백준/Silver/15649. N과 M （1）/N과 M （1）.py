import sys
input = sys.stdin.readline

def zz(level):
    if level == M:
        print(*path)
        return
    for i in range(N):
        if visited[i] != 0: continue
        visited[i] = i + 1
        path.append(i+1)
        zz(level + 1)
        path.pop()
        visited[i] = 0



N, M = map(int, input().split())
visited = [0] * N
path = []
zz(0)
