def dfs(Start):
    visited[Start] = 1
    for i in range(1, N + 1):
        if arr[Start][i] == 1 and visited[i] == 0:
            dfs(i)
    return


N = int(input())
T = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
result = 0

for t in range(T):
    A, B = map(int, input().split())
    arr[A][B] = 1
    arr[B][A] = 1

dfs(1)
for i in visited:
    result += i
print(result - 1)