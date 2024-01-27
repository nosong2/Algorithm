a=[]

for i in range(1,11):
    num=int(input())
    num%=42
    a.append(num)

a=set(a)
a=list(a)
print(len(a))
