import sys
from collections import deque

t = int(input())
Queue = deque([])

for i in range(1, t + 1):
    Queue.append(i)
while len(Queue) != 1:
    Queue.popleft()
    if len(Queue) != 1:
        Queue.append(Queue.popleft())
print(Queue[0])