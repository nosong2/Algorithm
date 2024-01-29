a=input()
b=a.upper()
dicti={}
aset=list(set(b))
max_count=[]
for i in aset:
    count=0
    for j in b:
        if i in j:
            count+=1

        dicti[i]=count            
    max_count.append(count)
max_max_count=max(max_count)

if max_count.count(max_max_count)>=2:
    print('?')
else:
    for key,value in dicti.items():
        if value ==max_max_count:
            print(key)