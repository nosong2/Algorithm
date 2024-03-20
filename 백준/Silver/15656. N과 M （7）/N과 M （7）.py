import sys
input = sys.stdin.readline

def dd(level, Start):
    if level == M:
        print(*path)
        return
    for i in range(N):
        # if visited[i] == 1:continue
        # visited[i] = 1
        path.append(oh[i])
        dd(level + 1, i)
        path.pop()
        # visited[i] = 0


N, M = map(int, input().split())
oh = list(map(int, input().split()))
oh.sort()
visited = [0] * N
path = []

dd(0, 0)
