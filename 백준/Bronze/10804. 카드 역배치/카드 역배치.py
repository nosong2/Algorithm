result = [i for i in range(1, 21)]
for j in range(10):
    S, E = map(int, input().split())
    S -= 1
    E -= 1
    level = 0
    let = E - S + 1
    while let // 2 != level:
        result[S], result[E] = result[E], result[S]
        S += 1
        E -= 1
        level += 1
print(*result)