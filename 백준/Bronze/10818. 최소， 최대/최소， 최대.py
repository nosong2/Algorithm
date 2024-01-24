n=int(input())
z=list(map(int,input().split()))
min=z[0]
max=z[0]
for i in z:
  if min<i: # 최소값
    min=min
  elif min>i:
    min=i
for j in z:
  if max<j: # 최대값
    max=j
  elif max>j:
    max=max
print(min,max)