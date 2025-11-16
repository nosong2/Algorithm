import sys

def factorial(num, result):
    if num == 1 or num == 0:
        print(result)
        return
    result = result * num
    factorial(num - 1, result)



t = int(input())

factorial(t, 1)

