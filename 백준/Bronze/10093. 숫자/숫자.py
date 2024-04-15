A, B = map(int, input().split())
if B > A:
    print(B - A - 1)
    for i in range(A + 1, B):
        print(i,end=' ')
elif A > B:
    print(A - B - 1)
    for i in range(B + 1, A):
        print(i,end=' ')
elif A == B:
    print(0)