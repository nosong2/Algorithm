a,b=map(int,input().split())
z=0
c=[]
v=[0]
for i in range(a):
    c=c+[i+1]

for j in range(b):
    q,w=map(int,input().split())
    v[0]=c[q-1]
    c[q-1]=c[w-1]
    c[w-1]=v[0]

for k in c:
    print(k,end=" ")