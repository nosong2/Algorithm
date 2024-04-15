import sys
input = sys.stdin.readline
from math import ceil

N = int(input())
money = list(map(int, input().split()))
Y = []
M = []
for i in range(N):
    Y.append(ceil(money[i]/30))
    M.append(ceil(money[i]/60))
    if money[i] % 30 == 0:
        Y.append(1)
    if money[i] % 60 == 0:
        M.append(1)
Yresult = sum(Y) * 10
Mresult = sum(M) * 15
if Yresult > Mresult:
    print('M', Mresult)
elif Yresult < Mresult:
    print('Y', Yresult)
else:
    print('Y', 'M', Yresult)