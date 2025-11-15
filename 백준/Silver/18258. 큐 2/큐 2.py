import sys
from collections import deque



t = int(input())
Queue = deque([])
result = []

for _ in range(t):
    word = input().split()
    if word[0] == 'push':
        Queue.append(word[1])
    elif word[0] == 'pop':
        if len(Queue) != 0: result.append(Queue.popleft())
        else: result.append('-1')
    elif word[0] == 'size': result.append(str(len(Queue)))
    elif word[0] == 'empty':
        if len(Queue) == 0: result.append('1')
        else: result.append('0')
    elif word[0] == 'front':
        if len(Queue) != 0: result.append(Queue[0])
        else: result.append('-1')
    elif word[0] == 'back':
        if len(Queue) != 0: result.append(Queue[-1])
        else: result.append('-1')

print('\n'.join(result))
