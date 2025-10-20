import sys

a = input()
b = input()

arr = [0] * 26
arr2 = [0] * 26
result = 0

for i in a:
    arr[ord(i)-97] += 1
for i in b:
    arr2[ord(i)-97] += 1
for i in range(26):
    if arr[i] != arr2[i]:
        result = result + abs(arr[i] - arr2[i])
print(result)