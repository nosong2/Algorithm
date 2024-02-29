N = int(input())
arr = list(map(int, input().split()))
result = []


for i in range(1, N + 1):
    result.insert(arr[i - 1],i)

print(*result[::-1])