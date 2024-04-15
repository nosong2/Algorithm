N = int(input())
cnt = N
for i in range(1, N * 2, 2):
    cnt -= 1
    star = i*'*'
    print(' '*cnt, end='')
    print(star)