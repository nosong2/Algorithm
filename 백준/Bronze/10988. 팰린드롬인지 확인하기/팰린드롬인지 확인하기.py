a=input()
val=list(a)
val.reverse()
b=''.join(val)
if a==b:
    print(1)
else:
    print(0)