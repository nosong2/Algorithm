import sys
input = sys.stdin.readline

N = int(input())
memo = [0, 1]

for i in range(2, abs(N) + 1):
    memo.append((memo[i - 1] + memo[i - 2]) % 1000000000)
if N > 0:
    print(1)
elif N == 0:
    print(0)
elif N < 0 and abs(N) % 2 == 0:
    print(-1)
elif N < 0 and abs(N) % 2 == 1:
    print(1)
print(memo[abs(N)])