import sys

t = int(input())
dic = {}

for i in range(t):
    human, how = input().split()
    if how == "enter":
        dic[human] = True
    elif how == "leave":
        del dic[human]

for name in sorted(dic.keys(), reverse=True):
    print(name)
