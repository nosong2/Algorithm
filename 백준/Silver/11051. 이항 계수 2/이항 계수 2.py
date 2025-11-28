import sys
from itertools import combinations

N, K = map(int, input().split())

pascal = [[0] * (i + 1) for i in range(N + 1)]
pascal[0] = [1]

for depth in range(1, N + 1):
    pascal[depth][0] = pascal[depth][-1] = 1
    for idx in range(1, depth):
        pascal[depth][idx] = pascal[depth - 1][idx - 1] + pascal[depth - 1][idx]

print(pascal[N][K] % 10007)
