N_arr = [list(map(int,input().split())) for _ in range(9)]
value = N_arr[0][0]
value_i = 0
value_j = 0

for i in range(9):
    for j in range(9):
        max_value = N_arr[i][j]
        if value <= max_value:
            value = max_value
            value_i = i + 1
            value_j = j + 1

print(value)
print(value_i, value_j)