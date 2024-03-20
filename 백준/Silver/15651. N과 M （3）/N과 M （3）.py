import sys
input = sys.stdin.readline

def dd(level):
    if level == M:
        print(*path)
        return
    for i in range(1, N + 1):
        path.append(i)
        dd(level + 1)
        path.pop()
N, M = map(int, input().split())
path = []

dd(0)
