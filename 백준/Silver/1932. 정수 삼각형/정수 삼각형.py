import sys

input = sys.stdin.readline

n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(n , 0, -1):
    for j in range(i - 1):
        # print(max(tri[i - 1][j], tri[i - 1][j + 1]))
        tri[i-2][j] = max(tri[i - 2][j] + tri[i - 1][j],tri[i - 2][j] + tri[i - 1][j + 1])
        # print(i - 1, j)
print(tri[0][0])
