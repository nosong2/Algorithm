import sys
from collections import deque

t, num = map(int, input().split())
checkarr = deque(map(int, input().split()))
result = 0
arr = deque(i for i in range(1, t + 1))
while checkarr:
    nowword = checkarr.popleft()
    while nowword != arr[0]:
        if arr.index(nowword) <= len(arr)//2:
            arr.rotate(-1)
            result += 1
        else:
            arr.rotate(1)
            result += 1
    if nowword == arr[0]:
        arr.popleft()
print(result)
