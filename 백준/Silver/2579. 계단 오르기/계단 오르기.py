import sys

input = sys.stdin.readline

n = int(input())
a = [0] + [int(input()) for _ in range(n)]  # 1-index

if n == 1:
    print(a[1])
elif n == 2:
    print(a[1] + a[2])
else:
    dp = [0] * (n + 1)
    dp[1] = a[1]
    dp[2] = a[1] + a[2]
    dp[3] = max(a[1] + a[3], a[2] + a[3])
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + a[i - 1]) + a[i]
    print(dp[n])
