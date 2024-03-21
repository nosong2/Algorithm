import sys
input = sys.stdin.readline

def johab(level, Start):
    if level == N:
        print(*path)
        return
    for i in range(Start, K):
        if visited[i] == 1: continue
        visited[i] = 1
        path.append(lotto[i])
        johab(level + 1, i + 1)
        path.pop()
        visited[i] = 0

while True:
    lotto = list(map(int, input().split()))
    if lotto == [0]: break
    N = 6
    M = lotto.pop(0)
    K = len(lotto)
    path = []
    visited = [0] * K

    johab(0, 0)
    print()
