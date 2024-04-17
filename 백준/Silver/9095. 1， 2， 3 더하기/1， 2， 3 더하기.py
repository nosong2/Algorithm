import sys
input = sys.stdin.readline

memo = [0] * 20
memo[1] = 1
memo[2] = 2
memo[3] = 4
memo[4] = 7
memo[5] = 13

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    for i in range(6, 20):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    print(memo[N])