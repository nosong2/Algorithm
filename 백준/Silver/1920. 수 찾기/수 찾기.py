import sys

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
Nlist.sort()
result = []

for num in Mlist:
    le, ri = 0, N - 1
    finds = False

    while le <= ri:
        mid = (le + ri) // 2
        if num == Nlist[mid]:
            finds = True
            print(1)
            break
        elif num > Nlist[mid]:
            le = mid + 1
        else:
            ri = mid - 1
    if not finds:
        print(0)
