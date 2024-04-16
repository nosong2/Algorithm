import sys
input = sys.stdin.readline

memo = [0] * 100
memo[0] = 0
memo[1] = 1
memo[2] = 1
memo[3] = 2

N = int(input())
for i in range(4, 100):
    memo[i] = memo[i - 1] + memo[i - 2]
print(memo[N])