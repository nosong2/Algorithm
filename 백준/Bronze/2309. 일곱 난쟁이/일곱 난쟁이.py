def little(x):
    global result
    if sum(path) > 100: return
    if x == 7 and sum(path) == 100:
        result.append(path[:])
        return
    else:
        for i in range(9):
            if visited[i] == 1:continue
            visited[i] = 1
            path.append(arr[i])
            little(x + 1)
            path.pop()
            visited[i] = 0


arr = []
T = 9
result = []
for t in range(T):
    path = []
    visited = [0] * T
    N = int(input())
    arr.append(N)

little(0)
result.sort(reverse=True)
real_result = result[0]
for i in range(6, -1, -1):
    print(real_result[i])
