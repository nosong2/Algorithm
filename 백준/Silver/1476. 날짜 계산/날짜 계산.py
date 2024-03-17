import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
a, b, c, count = 0, 0, 0, 0
while True:
    if a == E and b == S and c == M:
        break
    a += 1
    b += 1
    c += 1
    count += 1
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1

print(count)