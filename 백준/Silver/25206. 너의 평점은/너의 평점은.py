grades_dict = {'A+': 4.5,
               'A0': 4.0,
               'B+': 3.5,
               'A0': 4.0,
               'B+': 3.5,
               'B0': 3.0,
               'C+': 2.5,
               'C0': 2.0,
               'D+': 1.5,
               'D0': 1.0,
               'F' : 0.0}

sum = 0
sum2 = 0
grades = [list(map(str,input().split())) for _ in range(20)]
# 학점의 총합
for i in range(20):
    if grades[i][2] != 'P':
        sum += float(grades[i][1])

# 학점 x 과목평점
for j in range(20):
    for k in range(1,2):
        if grades[j][k+1] == 'P':
            continue
        else:
            sum2 += float(grades[j][k]) * grades_dict.get(grades[j][k+1])
print(sum2/sum)