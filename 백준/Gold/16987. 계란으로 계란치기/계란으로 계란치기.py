import sys

def checkpoint(arr):
    cnt = 0
    for i in arr:
        if i[0] <= 0:
            cnt += 1
    return cnt

def break_egg(depth, arrs):
    global result
    if depth == N:
        result = max(result, checkpoint(arrs))
        return
    if arrs[depth][0] <= 0:
        break_egg(depth + 1, arrs)
    else:
        nomore = True
        for i in range(N):
            if i != depth and arrs[i][0] > 0:
                nomore = False
                arrs[depth][0] -= arrs[i][1]
                arrs[i][0] -= arrs[depth][1]
                break_egg(depth + 1, arrs)
                arrs[depth][0] += arrs[i][1]
                arrs[i][0] += arrs[depth][1]
        if nomore:
            break_egg(N, arrs)


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
result = 0

break_egg(0, eggs)

print(result)