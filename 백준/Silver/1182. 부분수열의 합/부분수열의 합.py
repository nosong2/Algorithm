import sys
input = sys.stdin.readline

def gd(level, Start):
    global count, flag
    if flag == 1:
        if sum(path) == S:
            count += 1
    for i in range(Start, N):
        path.append(arr[i])
        flag = 1
        gd(level + 1, i + 1)
        path.pop()

N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
path = []
count = 0
flag = 0

gd(0, 0)

print(count)