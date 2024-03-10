#이 코드는 문제 풀고 나서, 다른 사람의 다른 방식을 보면서 한 것, 개인공부용이고 내 실력이 아님

import sys
input = sys.stdin.readline

def dfs(home_i, home_j):
    global result
    if abs(home_i - festival_i) + abs(home_j - festival_j) <= 1000:
        result = 'happy'
    #가지치기
    for i in mart:
        if i[2]: continue
        if abs(home_i - i[0]) + abs(home_j - i[1]) <= 1000:
            i[2] = 1
            dfs(i[0], i[1])


T = int(input())
for t in range(T):
    N = int(input()) # 편의점 갯수
    home_i, home_j = map(int, input().split())
    mart = [list(map(int, input().split() + [0])) for _ in range(N)]
    festival_i, festival_j = map(int, input().split())
    result = 'sad'

    dfs(home_i, home_j)

    print(result)