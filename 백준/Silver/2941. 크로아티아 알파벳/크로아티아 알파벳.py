text = input()
pattern = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in pattern:
    if i in text:
        text = text.replace(i,'1')
print(len(text))