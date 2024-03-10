import sys
from collections import deque
input = sys.stdin.readline

def happy_check(festival_i, festival_j):
    global result
    for _ in range(len(mart)):
        i, j = mart.popleft()
        if abs(festival_i - i) + abs(festival_j - j) <= 1000:
            happy_mart.append([i, j])
            mart.append([i, j])
        else:
            mart.append([i, j])
    while happy_mart:
        q, w = happy_mart.popleft()
        if q == home_i and w == home_j:
            result = 'happy'
            return
        visited[mart.index([q, w])] = 1
        for l in mart:
            if abs(q - l[0]) + abs(w - l[1]) <= 1000 and visited[mart.index([l[0], l[1]])] == 0:
                happy_mart.append([l[0], l[1]])
    result = 'sad'
    return


T = int(input())
for t in range(T):
    result = ''
    N = int(input()) # 편의점 갯수
    mart = deque() # 편의점 리스트
    happy_mart = deque() # 갈 수 있는 편의점 리스트
    Queue = deque()
    home_i, home_j = map(int, input().split())
    for _ in range(N): # 편의점
        x, y = map(int, input().split())
        mart.append([x, y])
    mart.append([home_i, home_j])
    visited = [0] * (len(mart) + 1)
    festival_i, festival_j = map(int, input().split())

    happy_check(festival_i, festival_j)

    print(result)