import sys
from collections import deque

n, k = map(int, input().split())

time = [0] * 100001
temp = [0] * 100001
arr = []

def movesubin(x):
    while True:
        arr.append(x)
        if x == n:
            return
        x = temp[x]

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()

        if x == k:
            movesubin(x)
            return
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and time[i] == 0:
                queue.append(i)
                time[i] = time[x] + 1
                temp[i] = x

bfs()
print(len(arr) - 1)

for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
