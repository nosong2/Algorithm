import sys

x = int(input())
back = True

while True:
    for i in range(2, x + 1):
        if x % i == 0:
            x = x // i
            print(i)
            break
    if x == 1:
        back = False
    elif x == 2 or x == 3:
        print(x)
        back = False
    if not back:
        break
