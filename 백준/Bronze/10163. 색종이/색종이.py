arr = [[0] * 1001 for _ in range(1001)]
N = int(input())

for n in range(1, N + 1):
    i, j, x, y = map(int, input().split())
    for i in range(x):
        for j in range(y):
            arr[i][j] += 1


for n in range(1, N + 1):
    count = 0
    for i in arr:
        for j in i:
            if j == n:
                count += 1

    print(count)