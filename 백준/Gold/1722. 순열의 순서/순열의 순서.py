import sys
from math import factorial

N = int(input())
arr = list(map(int, input().split()))

nums = list(range(1, N + 1))

if arr[0] == 1:
    k = arr[1]
    used = [False] * (N + 1)
    result = []
    k -= 1
    for i in range(N):
        fact = factorial(N - i - 1)
        for j in range(1, N + 1):
            if used[j]:
                continue
            if k >= fact:
                k -= fact
            else:
                result.append(j)
                used[j] = True
                break
    print(*result)
else:
    seq = arr[1:]
    used = [False] * (N + 1)
    order = 1
    for i in range(N):
        fact = factorial(N - i - 1)
        count = 0
        for j in range(1, seq[i]):
            if not used[j]:
                count += 1
        order += count * fact
        used[seq[i]] = True
    print(order)