import sys
input = sys.stdin.readline

M = int(input())
A = []
total = 0
xor = 0
for m in range(M):
    num = list(map(int, input().split()))
    if num[0] == 1:
        total += num[1]
        xor = xor ^ num[1]
    elif num[0] == 2:
        total -= num[1]
        xor = xor ^ num[1]
    elif num[0] == 3:
        print(total)
    elif num[0] == 4:
        print(xor)