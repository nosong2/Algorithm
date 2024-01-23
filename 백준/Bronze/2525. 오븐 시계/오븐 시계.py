a,b=map(int,input().split())
c=int(input())
b=b+c
while b>=60:
    if b>=60:
        a+=1
        b=b-60
        if a>=24:
            a=0
print(a, b)