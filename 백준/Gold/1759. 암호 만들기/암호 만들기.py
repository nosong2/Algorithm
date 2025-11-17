import sys
from itertools import combinations

n, t = map(int, input().split())
checking = ["a", "e", "i", "o", "u"]
secret = input().split()
secret.sort()
for a in combinations(secret, n):
    z = sum(1 for ch in a if ch in checking)
    x = n - z
    if z >= 1 and x >= 2: print("".join(a))