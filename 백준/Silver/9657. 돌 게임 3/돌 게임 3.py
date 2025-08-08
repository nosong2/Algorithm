import sys


n = int(input().strip())

print("CY" if n % 7 in (0, 2) else "SK")
