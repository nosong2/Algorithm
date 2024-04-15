N = int(input())
for i in range(N, -1, -1):
    star = i*'*'
    print(star.rjust(N))