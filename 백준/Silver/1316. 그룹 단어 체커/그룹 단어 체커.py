T = int(input())
count = T
for t in range(T):
    N = input()
    for j in range(len(N)-1):
        if N[j] != N[j+1] and N[j] in N[j+1:]:
            count -= 1
            break

print(count)