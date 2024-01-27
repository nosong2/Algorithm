import copy

def coandre(x,y):
    y=copy.deepcopy(x)
    y.reverse()
    return y

a, b= map(int,input().split())
basket=[]
basket2=[]
for i in range(1,a+1):
    basket.append(i)
basket2=coandre(basket,basket2)

for j in range(b):
    c, d=map(int,input().split())
    if c==1:
        basket[c-1:d]=basket2[-d:]
        basket2=coandre(basket,basket2)
    elif c!=1:
        basket[c-1:d]=basket2[-d:-c+1]
        basket2=coandre(basket,basket2)

for k in basket:
    print(k,end=' ')