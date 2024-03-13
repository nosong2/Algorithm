import sys
input = sys.stdin.readline



T = int(input())
for t in range(T):
    money = 0
    N = int(input())
    stork = list(map(int, input().split()))
    stork.reverse()
    first_value = stork[0]
    for i in range(1, N):
        if first_value > stork[i]:
            money += (first_value - stork[i])
        elif first_value <= stork[i]:
            first_value = stork[i]
    print(money)