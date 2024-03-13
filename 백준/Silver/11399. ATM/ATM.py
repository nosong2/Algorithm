import sys
input = sys.stdin.readline

T = int(input())
person = list(map(int, input().split()))
sum = 0
result = 0
person.sort()
for i in person:
    sum = sum + i
    result += sum
print(result)