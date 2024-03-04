di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(x, y):
    global count
    visited[x][y] = 1
    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == 1:
            dfs(ni, nj)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 0
flag = 0
save = []
result = [0]
sum = 0
lastsum = 0

while not flag:
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and visited[i][j] == 0:
                save.append([i, j])
    if not save:
        flag = 1
        break
    dfs(*save.pop(0))
    save = []

    for i in range(N):
        for j in range(N):
            sum += visited[i][j]
    for i in range(len(result)):
        sum -= result[i]
    result.append(sum)
    result.sort()
    sum = 0
    count += 1
print(count)
for i in range(1, count + 1):
    print(result[i])