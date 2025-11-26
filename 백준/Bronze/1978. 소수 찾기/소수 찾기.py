import sys

t = int(input())
num = list(map(int, input().split()))
cnt = 0

for i in num:
    now = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            now = False
            break
    if now == True:
        cnt += 1
print(cnt)