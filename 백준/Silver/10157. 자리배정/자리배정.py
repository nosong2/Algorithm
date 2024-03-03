def dd():
    new_i = 0
    new_j = 0
    count = 1
    for i in range(C):
        for j in range(R):
            for k in range(4):
                while 0 <= new_i + di[k] < C and 0 <= new_j + dj[k] < R and arr[new_j + dj[k]][new_i + di[k]] == 0:
                    count += 1
                    new_i += di[k]
                    new_j += dj[k]
                    arr[new_j][new_i] = count

                    if arr[new_j][new_i] == K:
                        result.append(new_i)
                        result.append(new_j)
                        return result

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

C, R = map(int, input().split())
K = int(input())
arr = [[0] * C for _ in range(R)]
result = []
arr[0][0] = 1

dd()
if K == 1:
    result.append(0)
    result.append(0)
if len(result) == 0:
    print(0)
else:
    for a in range(2):
        print(result[a] + 1,end=' ')