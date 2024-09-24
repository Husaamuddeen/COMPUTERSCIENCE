'''Challenge: 
Write a program that calculates the factorial of a given number.
Define a function called factorial that takes an integer as input and returns its factorial.
Call this function to compute the factorial of a number entered by the user'''

def findFactorial (num):
    factorial = 1
    for i in range(0,num-1):
        factorial = factorial*(num-i)
    return factorial
number = int(input('enter a number: '))
print('the factorial of your number is: '+ str(findFactorial(number)))