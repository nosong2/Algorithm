import sys
input = sys.stdin.readline
from math import ceil

N = int(input()) # 시험장 갯수
student = list(map(int, input().split()))
B, C = map(int, input().split())
result = N
for i in range(N):
    if student[i]-B > 0:
        result += ceil((student[i]-B)/C)
    else:
        continue

print(result)