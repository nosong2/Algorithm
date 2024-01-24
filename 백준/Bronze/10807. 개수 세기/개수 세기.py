n=int(input())
z=list(map(int,input().split()))
v=int(input())
sum=0
for i in z:
  if i==v:
    sum+=1
print(sum)