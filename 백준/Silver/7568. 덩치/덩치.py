import sys
input = sys.stdin.readline

T = int(input())
person = []
copyperson = []
for t in range(T):
    q, w = map(int, input().split())
    person.append([q, w, 0])
    copyperson.append([q, w])

for j in range(T):
    rate = 1
    a = copyperson.pop()
    for i in person:
        if a[0] < i[0] and a[1] < i[1]:
            rate += 1
    person[T - j - 1][2] = rate

for i in range(T):
    print(person[i][2], end=' ')
