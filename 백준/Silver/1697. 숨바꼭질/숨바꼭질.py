def bfs(N, K):
    Queue = []
    visited[N] = 1
    Queue.append(N)
    while Queue:
        x = Queue.pop(0)
        if x == K:
            print(visited[x] - 1)
            return
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                Queue.append(i)

N, K = map(int, input().split())
visited = [0] * 100001
bfs(N, K)