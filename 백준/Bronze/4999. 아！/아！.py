import sys
input = sys.stdin.readline

N = input()
doctor = input()
if len(N) >= len(doctor):
    print('go')
else:
    print('no')
