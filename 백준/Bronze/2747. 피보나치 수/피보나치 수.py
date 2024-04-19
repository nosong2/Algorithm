import sys
input = sys.stdin.readline

N = 50
M = int(input())
memo = [0] * 50
memo[0] = 0
memo[1] = 1
memo[2] = 1

for i in range(3, N):
    memo[i] = memo[i - 1] + memo[i - 2]
print(memo[M])