arr = [[0] * 100 for _ in range(100)]
aa = 0
for t in range(4):
    x, y, X, Y = map(int, input().split())
    for i in range(y, Y):
        for j in range(x, X):
            arr[i][j] = 1
for i in arr:
    aa += sum(i)
print(aa)