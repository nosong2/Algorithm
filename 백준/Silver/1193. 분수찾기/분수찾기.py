import sys

t = int(input())

arr = [1]
turn = 1
start = 1
while t >= start + turn:
    start += turn
    turn += 1
    arr.append(start)
if len(arr)%2 == 1 and len(arr) != 1:
    result_left = len(arr)
    result_right = 1
    whoami = True
else:
    result_left = 1
    result_right = len(arr)
    whoami = False

if whoami:
    while t != start:
        start += 1
        result_left -= 1
        result_right += 1
else:
    while t != start:
        start += 1
        result_left += 1
        result_right -= 1

print(result_left, end="")
print("/", end="")
print(result_right)