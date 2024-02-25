def dfs(Start):
    global result
    visited[Start] = 1
    print(Start, end=' ')
    for i in range(1, N + 1):
        if arr[Start][i] == 1 and visited[i] == 0:
            result.append(i)
            dfs(i)

def bfs(Start):
    Queue = []
    visited1[Start] = 1
    Queue.append(Start)
    while Queue:
        Start = Queue.pop(0)
        print(Start, end = ' ')
        for i in range(1, N + 1):
            if visited1[i] == 0 and arr[Start][i] == 1:
                Queue.append(i)
                visited1[i] = 1

N, M, V = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
result = [V]

arr1 = [[] for _ in range(N + 1)]
visited1 = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    arr[A][B] = 1
    arr[B][A] = 1
    arr1[A].append(B)
    arr1[B].append(A)
dfs(V)
print()
bfs(V)