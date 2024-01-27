a=int(input())
examsum=0
exam=[]
b=list(map(float,input().split()))
for i in range(a):
    exam.append(b[i])
maxexam=max(exam)

for j in exam:
    sum=(j/maxexam*100/a)
    examsum+=sum
print(examsum)