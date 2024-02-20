dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    #enQ
    Queue = []
    #튜플로 묶든, 리스트로 묶든 묶어야함
    Queue.append([x, y])
    #방문표시
    visited[x][y] = 1
    while Queue:
        # deQ
        x, y = Queue.pop(0)
        if x + 1 == N and y + 1 == M:
            return visited[x][y]
        #해야 할 일
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
                Queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

print(bfs(0, 0))