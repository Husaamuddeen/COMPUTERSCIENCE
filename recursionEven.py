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
print(calcSum(40))
