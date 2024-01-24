z=[]
for i in range(9):
  z.append(int(input()))
print(max(z))
print(z.index(max(z))+1)