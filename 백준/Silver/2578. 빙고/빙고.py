def bingo(reresult):
    bingo = 0
    count = 0
#가로
    for i in range(N):
        if visited[i][0] == 1:
            for j in range(1, N):
                if visited[i][j] == 1:
                    count += 1
        if count == 4:
            count -= 4
            bingo += 1
        else:
            count = 0
#세로
    for i in range(N):
        if visited[0][i] == 1:
            for j in range(1, N):
                if visited[j][i] == 1:
                    count += 1
        if count == 4:
            count -= 4
            bingo += 1
        else:
            count = 0
#대각선
    for i in range(N):
        if visited[i][i] == 1:
            count += 1
    if count == 5:

        count -= 5
        bingo += 1
    else:
        count = 0
#다른 대각선
    for i in range(N):
        if visited[0 + i][N - 1 - i] == 1:
            count += 1
    if count == 5:
        count -= 5
        bingo += 1
    else:
        count = 0
#검사
    if bingo >= 3:
        reresult += 1
        return reresult
N = 5
result = [list(map(int, input().split())) for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
arrr = []
real = 0

for i in range(N):
    for j in range(N):
        arrr.append(arr[i][j])
for k in range(25):

    go = arrr.pop(0)
    for i in range(N):
        for j in range(N):
            if result[i][j] == go:
                visited[i][j] = 1
                if bingo(0) == 1 and real == 0:
                    real = k + 1

print(real)