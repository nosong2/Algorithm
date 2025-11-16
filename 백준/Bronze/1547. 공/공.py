import sys

def rolling(a, b):
    global ball
    if ball == a:
        ball = b
    elif ball == b:
        ball = a
    return

t = int(input())
ball = 1
for _ in range(t):
    x, y = map(int, input().split())
    rolling(x, y)
print(ball)