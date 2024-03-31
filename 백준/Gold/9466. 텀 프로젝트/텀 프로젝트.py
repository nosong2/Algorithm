import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def zz(num):
    global cnt
    visited[num] = 1
    aa.append(num)
    if visited[stu[num]] == 1:
        if stu[num] in aa:
            cnt += len(aa[aa.index(stu[num]):])
        return
    zz(stu[num])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    stu = [0] + list(map(int, input().split()))
    team = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    cnt = 0
    # print(stu)
    # for i in range(1, N + 1):
    #     team[i].append(stu[i])

    for j in range(1, N + 1):
        if visited[j] == 0:
            aa = []
            zz(j)
    print(N - cnt)