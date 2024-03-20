import sys
input = sys.stdin.readline

def dd(level, Start):
    global flag
    if level == M:
        result.append(path[:])
        return
    for i in range(N):
        if visited[i] == 1:continue
        visited[i] = 1
        path.append(oh[i])
        dd(level + 1, i)
        path.pop()
        visited[i] = 0


N, M = map(int, input().split())
oh = list(map(int, input().split()))
oh.sort()
visited = [0] * N
path = []
result = []

dd(0, 0)
result = sorted(list(set(map(tuple, result))))

for i in result:
    print(*i)
