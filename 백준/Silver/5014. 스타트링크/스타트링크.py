import sys
from collections import deque

#F 건물 층
#S 출발점
#G 스타트링크(도착지)
#U 한번에 올라갈 수 있는 값
#D 한번에 내려갈 수 있는 값
def bfs(Start, Up, Down):
    Queue = deque()
    visited[Start] = 1
    Queue.append(Start)
    while Queue:
        x = Queue.popleft()
        if x == G:
            print(visited[x] - 1)
            return
        for i in (x + Up, x - Down):
            if 0 < i < (F + 1) and visited[i] == 0:
                visited[i] = visited[x] + 1
                Queue.append(i)
    return print('use the stairs')


F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)

bfs(S, U, D)