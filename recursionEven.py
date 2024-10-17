def addEvens(n):
    if n >= 4:
        sum = n + addEvens(n-2)
    else:
        sum = n
    return sum

def calcSum(n):
    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibonacci2(n):
    fibNumbers = [0,1]
    for i in range(2,n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]

n = int(input('enter term: '))
import time
startTime = time.perf_counter()
print(fib(n))
endTime = time.perf_counter()
print(endTime-startTime)
startTime = time.perf_counter()
print(fibonacci2(n))
endTime = time.perf_counter()
print(endTime-startTime)