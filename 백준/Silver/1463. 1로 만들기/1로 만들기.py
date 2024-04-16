memo = [0] * 1000010
memo[0] = 0
memo[1] = 0
N = int(input())

for i in range(2, N + 2):
    memo[i] = memo[i-1] + 1
    if i % 2 == 0 and memo[i] > memo[i // 2] + 1:
        memo[i] = memo[i // 2] + 1
    if i % 3 == 0 and memo[i] > memo[i // 3] + 1:
        memo[i] = memo[i // 3] + 1
print(memo[N])
