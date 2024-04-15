N = int(input())
cnt = 0
for i in range(N * 2 - 1, -2, -2):
    star = i*'*'
    print(' '*cnt, end='')
    print(star)
    cnt += 1