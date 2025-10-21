import sys, math

t, maxstu = map(int, input().split())

room = [[0] * 6, [0] * 6]
result = 0

for i in range(t):
    sex, level = map(int, input().split())
    room[sex][level - 1] += 1
for i in range(2):
    for j in range(6):
        result = result + math.ceil(room[i][j] / maxstu)

print(result)