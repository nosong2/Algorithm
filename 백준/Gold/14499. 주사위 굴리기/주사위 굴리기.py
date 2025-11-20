import sys

def dice(num, arr):
    global x, y
    # 동쪽
    if num == 1 and y + 1 < m:
        y += 1
        if dos[x][y] == 0: dos[x][y] = arr[3]
        else:
            arr[3] = dos[x][y]
            dos[x][y] = 0
        print(arr[2])
        return [arr[3], arr[1], arr[0], arr[5], arr[4], arr[2]]
    # 서쪽
    elif num == 2 and y - 1 >= 0:
        y -= 1
        if dos[x][y] == 0: dos[x][y] = arr[2]
        else:
            arr[2] = dos[x][y]
            dos[x][y] = 0
        print(arr[3])
        return [arr[2], arr[1], arr[5], arr[0], arr[4], arr[3]]
    # 북쪽
    elif num == 3 and x - 1 >= 0:
        x -= 1
        if dos[x][y] == 0: dos[x][y] = arr[4]
        else:
            arr[4] = dos[x][y]
            dos[x][y] = 0
        print(arr[1])
        return [arr[4], arr[0], arr[2], arr[3], arr[5], arr[1]]
    # 남쪽
    elif num == 4 and x + 1 < n:
        x += 1
        if dos[x][y] == 0: dos[x][y] = arr[1]
        else:
            arr[1] = dos[x][y]
            dos[x][y] = 0
        print(arr[4])
        return [arr[1], arr[5], arr[2], arr[3], arr[0], arr[4]]
    else:
        return arr


a = [0, 0, 0, 0, 0, 0]

n, m, x, y, t = map(int, input().split())
dos = [list(map(int, input().split())) for _ in range(n)]
trys = list(map(int, input().split()))

for i in range(t):
    a = dice(trys[i], a)
