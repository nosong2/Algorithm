k = int(input())
l = []
l_no = []
max_h = 0
max_w = 0

for m in range(6):
    i, j = map(int, input().split())
    l.append(j)
    if i >= 3 and max_h < j:
        max_h = j
        max_h_idx = m
    elif i <= 2 and max_w < j:
        max_w = j
        max_w_idx = m

l_no.append(max_w_idx)
l_no.append(max_h_idx)

temp = max_w_idx - 1
if temp < 0:
    temp += 6
l_no.append(temp)
temp = max_w_idx + 1
if temp > 5:
    temp -= 6
l_no.append(temp)
temp = max_h_idx - 1
if temp < 0:
    temp += 6
l_no.append(temp)
temp = max_h_idx + 1
if temp > 5:
    temp -= 6
l_no.append(temp)

square = 1
for i in range(6):
    if i not in l_no:
        square *= l[i]

print((max_w * max_h - square)*k)