import sys
input = sys.stdin.readline

T = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
sum = 0

for t in range(T):
    sum += A[t]*B[t]
print(sum)