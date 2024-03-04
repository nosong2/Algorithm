def dfs(Start, End):
    global count
    count += 1
    if visited[End] == 1:
        return count
    # for i in range(len(family[Start])):
    #     if visited[family[Start][i]] == 0:
    #         visited[i] = visited[Start] + 1
    #         dfs(family[Start][i], End)
    for i in family[Start]:
        if visited[i] == 0:
            visited[i] = visited[Start] + 1
            dfs(i, End)

L = int(input())
family = [[] for _ in range(L + 1)]
N, M = map(int, input().split())
visited = [0] * (L + 1)
count = 0
T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
dfs(N, M)

if visited[M] == 0:print(-1)
else: print(visited[M])