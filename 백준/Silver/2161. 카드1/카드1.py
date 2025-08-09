import sys
from collections import deque

input = sys.stdin.readline

card = int(input())
dq = deque(range(1, card + 1))
ans = deque()
left = deque()

while len(dq) > 1:
    ans.append(dq.popleft())
    dq.append(dq.popleft())


print(*ans, *dq)