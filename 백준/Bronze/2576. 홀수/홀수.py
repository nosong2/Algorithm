result = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        result.append(num)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))