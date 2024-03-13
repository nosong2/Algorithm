import sys
input = sys.stdin.readline

N = int(input())
hoeyee = []
count = 1
for _ in range(N):
    q, w = map(int, input().split())
    hoeyee.append([q, w])
hoeyee.sort()
hoeyee = sorted(hoeyee, key=lambda x:x[1])

x = hoeyee.pop(0)
value = x[1]
for i in hoeyee:
    if value <= i[0]:
        value = i[1]
        count += 1
print(count)