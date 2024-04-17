import sys
input = sys.stdin.readline

N = 40
zero_memo = [0] * (N + 1)
one_memo = [0] * (N + 1)
zero_memo[0] = 1
zero_memo[1] = 0
one_memo[0] = 0
one_memo[1] = 1

for i in range(2, N + 1):
    zero_memo[i] = zero_memo[i - 1] + zero_memo[i - 2]
    one_memo[i] = one_memo[i - 1] + one_memo[i - 2]

T = int(input())
for t in range(1, T + 1):
    M = int(input())
    print(zero_memo[M], one_memo[M])