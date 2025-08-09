import sys

input = sys.stdin.readline

def tetro(i, j):
    global highmax
    # 네모
    if i + 1 < y and j + 1 < x:
        highmax = max(highmax, arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1])
    # 2 x 3
    if i + 1 < y and j + 2 < x:
        highmax = max(highmax,
            arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2],
            arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2],
            arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2],
            arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i][j + 2],
            arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2],
            arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i][j + 2],
            arr[i + 1][j] + arr[i + 1][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2],
            arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i][j + 2],
            )
    # 3 x 2
    if i + 2 < y and j + 1 < x:
        highmax = max(highmax,
            arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i][j + 1],
            arr[i + 2][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1],
            arr[i + 1][j] + arr[i + 2][j] + arr[i][j + 1] + arr[i + 1][j + 1],
            arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1],
            arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j],
            arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1],
            arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1],
            arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1],
            )
    # 길쭉이 가로
    if i + 3 < y:
        highmax = max(highmax,
            arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j])
    # 길쭉이 세로
    if j + 3 < x:
        highmax = max(highmax,
            arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3])
        # print(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3])
    return

y, x = map(int,input().split())

highmax = 0

arr = [list(map(int, input().split())) for _ in range(y)]

for i in range(y):
    for j in range(x):
        tetro(i, j)

print(highmax)
