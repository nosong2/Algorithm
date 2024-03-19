import sys
input = sys.stdin.readline

N = int(input())
M = str(N)
q = 0
for i in range( 10**len(M)):
    result = i
    x = list(str(i))
    for j in range(0, len(x)):
        result += int(x[j])
    if N == result:
        q = i
        break
if q != 0:
    print(i)
else:
    print(q)