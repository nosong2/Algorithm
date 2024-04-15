import sys
input = sys.stdin.readline

docu = input().strip()
search = input().strip()
top = 0
result = 0
while top <= len(docu)-len(search):
    if search == docu[top:top + len(search)]:
        result += 1
        top += len(search)
    elif search != docu[top:top + len(search)]:
        top += 1
print(result)