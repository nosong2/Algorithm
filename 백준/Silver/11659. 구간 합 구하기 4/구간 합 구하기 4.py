import sys

input = sys.stdin.readline

n, j = map(int,input().split())

arr = list(map(int, input().split()))

result = [0] * (n + 1)
for i in range(1, n + 1):
    result[i] = result[i - 1] + arr[i - 1]

for j in range(j):
    a, b = map(int, input().split())
    print(result[b] - result[a - 1])