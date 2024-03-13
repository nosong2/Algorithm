import sys
input = sys.stdin.readline

a = []
max_value = 0
T = int(input())
for t in range(T):
    x = int(input())
    a.append(x)
a.sort()

for i in a:
    if max_value < i * T:
        max_value = i * T
    T -= 1
print(max_value)