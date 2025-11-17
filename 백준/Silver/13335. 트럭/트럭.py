import sys
from collections import deque
from itertools import combinations

truck, ranger, limit = map(int, input().split())
trucks = deque(map(int, input().split()))
weight = 0
result = 0
now = deque()

while trucks or now:

    if trucks and weight + trucks[0] <= limit:
        newtruck = trucks.popleft()
        weight += newtruck
        now.append([newtruck, 0])
    for _ in range(len(now)):
        a = now.popleft()
        a[1] += 1
        if a[1] < ranger:
            now.append(a)
        else:
            weight -= a[0]
    result += 1

print(result + 1)
