

result = 0
N = str(input())
M = N.split('-')
result = sum(map(int, (M[0].split('+'))))

for k in M[1:]:
    k = sum(map(int, (k.split('+'))))
    result -= k
print(result)