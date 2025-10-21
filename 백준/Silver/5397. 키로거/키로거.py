import sys
from collections import deque


t = int(input())


for _ in range(t):
    leftarr = deque()
    rightarr = deque()
    n = deque(input().strip())
    while n:
        word = n.popleft()
        if word == "<" and len(leftarr) != 0:
            rightarr.append(leftarr.pop())
        elif word == ">" and len(rightarr) != 0:
            leftarr.append(rightarr.pop())
        elif word == "-" and len(leftarr) != 0:
            leftarr.pop()
        elif word != "<" and word != ">" and word != "-":
            leftarr.append(word)
            
    
    for i in leftarr:
        print(i, end="")
    rightarr.reverse()
    for i in rightarr:
        print(i, end="")
    print()
