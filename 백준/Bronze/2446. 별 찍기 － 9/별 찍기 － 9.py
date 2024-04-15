N = int(input())
cnt = N * 2 - 1
cnt2 = 0
flag = 0
for i in range(2*N-1):
    print(' '*cnt2,end='')
    print('*'*cnt)
    if flag == 0:
        cnt -= 2
        cnt2 += 1
    elif flag == 1:
        cnt += 2
        cnt2 -= 1
    if cnt < 0:
        cnt += 4
        cnt2 -= 2
        flag += 1