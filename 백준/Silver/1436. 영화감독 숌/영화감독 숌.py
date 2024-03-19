import sys
input = sys.stdin.readline

N = int(input())
count = 0
for i in range(1, 10**7):
    if '666' in str(i):
        count += 1
    if count == N:
        print(i)
        break