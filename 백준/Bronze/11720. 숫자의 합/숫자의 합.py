a=int(input())
b=list(map(int,input()))
c=0

for i in range(a):
    c+=b[i]
print(c)