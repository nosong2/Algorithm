sum=0
a={'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
num=input()
for i,val in a.items():
    for j in num:
        if j in i:
            sum+=val
print(sum)