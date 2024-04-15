A = int(input())
B = int(input())
C = int(input())
value = A*B*C
value = str(value)
result = [0] * 10
for i in value:
    result[int(i)] += 1
for i in result:
    print(i)