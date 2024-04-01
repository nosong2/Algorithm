import sys
input = sys.stdin.readline

def soon(level):
    global result
    if level == M:
        team = path[:3] + [0] + path[3:]
        # 야구하기
        number = 0
        point = 0
        for inni in person:
            p1 = p2 = p3 = 0
            out = 0
            while out < 3:
                if inni[team[number]] == 0: # 아웃
                    out += 1
                elif inni[team[number]] == 1:
                    point += p3
                    p1, p2, p3 = 1, p1, p2
                elif inni[team[number]] == 2:
                    point += p3 + p2
                    p1, p2, p3 = 0, 1, p1
                elif inni[team[number]] == 3:
                    point += p3 + p2 + p1
                    p1, p2, p3 = 0, 0, 1
                elif inni[team[number]] == 4:
                    point += p3 + p2 + p1 + 1
                    p1 = p2 = p3 = 0
                number += 1
                if number == 9:
                    number = 0
        result = max(result, point)

    for j in range(M):
        if random[j] in path: continue
        path[level] = random[j]
        soon(level + 1)
        path[level] = 0



N = int(input())
M = 8
person = [list(map(int, input().split())) for _ in range(N)]
random = [i for i in range(1, 9)]
path = [0] * 8
result = 0

x = 0

soon(0) # 야구 한번 조합돌기

print(result)
