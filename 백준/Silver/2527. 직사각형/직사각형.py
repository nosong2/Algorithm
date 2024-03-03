for _ in range(4):
    x, y, p, q, x2, y2, p2, q2 = map(int, input().split())
    if p < x2 or x > p2 or y > q2 or q < y2:
        print('d')
    elif (p == x2 and y == q2) or (p == x2 and q == y2) or (x == p2 and q == y2) or (x == p2 and y == q2):
        print('c')
    elif q2 == y or y2 == q:
        # if x <= x2 <= p or x <= p2 <= p:
        print('b')
    elif x2 == p or p2 == x:
        # if y <= y2 <= q or y <= q2 <= q:
        print('b')
    else:
        print('a')