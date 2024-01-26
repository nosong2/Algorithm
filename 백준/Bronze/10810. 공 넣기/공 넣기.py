a,b=map(int,input().split())

c=[]
for i in range(a):
    c=c+[0]


for j in range(b):
    q,w,e=map(int,input().split())
    for o in range(q,w+1):
        c[o-1]=e

for k in c:
    print(k,end=" ")