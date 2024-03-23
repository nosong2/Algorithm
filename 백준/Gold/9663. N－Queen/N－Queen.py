# 어려워서 문어선생님 풀이를 참고했습니다... 공부용

import sys
input = sys.stdin.readline

def dfs(level):
    global cnt
    if level == N:
        cnt += 1
        return
    for i in range(N):
        if visited[i] == visited1[level - i] == visited2[level + i] == 0:
            visited[i] = 1
            visited1[level - i] = 1
            visited2[level + i] = 1
            dfs(level + 1)
            visited[i] = 0
            visited1[level - i] = 0
            visited2[level + i] = 0


N = int(input())
visited = [0] * N # 수직 아래
visited1 = [0] * (2 * N) # 우 하 대각
visited2 = [0] * (2 * N) # 좌 하 대각

cnt = 0

dfs(0)

print(cnt)