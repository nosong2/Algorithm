import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0] # 북 동 남 서
dj = [0, 1, 0, -1]

def find_direct(i, j, d): # 현재 청소기 위치, 방향
    global result
    count = 0
    result += 1
    if room[i][j] == 1:
        print(result)
        return
    for k in range(4):
        ni = i + di[d - k - 1]  # k값 조절, 방향값 빼서 방향에따라 우선 탐색 순서가 바뀌게 설정
        nj = j + dj[d - k - 1]
        if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            return ni, nj, (d - k + 3) % 4
        elif 0 <= ni < N and 0 <= nj < M and (room[ni][nj] == 1 or visited[ni][nj] == 1):
            count += 1
    if count == 4: # 후진
        if d == 0:
            result -= 1
            return i + 1, j, d
        elif d == 1:
            result -= 1
            return i, j - 1, d
        elif d == 2:
            result -= 1
            return i - 1, j, d
        elif d == 3:
            result -= 1
            return i, j + 1, d
'''
3 3 방의 크기 N, M
1 1 0 로봇청소기의 좌표(1,1) 방향(북:0, 동1, 남2, 서3)
1 1 1 방의 상태(청소 안된 빈 칸 : 0, 기둥 : 1)
1 0 1
1 1 1
'''

N, M = map(int, input().split())
i, j, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 1
visited[i][j] = 1

while room[i][j] != 1:
    i, j, d = find_direct(i, j, d)
print(result)