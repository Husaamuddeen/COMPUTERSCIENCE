def addEvens(n):
    if n >= 4:
        sum = n + addEvens(n-2)
    else:
        sum = n
    return sum

def calcSum(n):
    i = 1
    while i < n:
        i = 2*i + 1
    return i
print(calcSum(40))
