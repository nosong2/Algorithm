import sys
input = sys.stdin.readline

N = int(input())
level_list = []
count = 0
for i in range(N):
    level = int(input())
    level_list.append(level)
max_level = level_list.pop()
min_level = level_list.pop()

while True:
    while max_level <= min_level:
        min_level -= 1
        count += 1
    if not level_list:
        break
    max_level = min_level
    min_level = level_list.pop()

print(count)