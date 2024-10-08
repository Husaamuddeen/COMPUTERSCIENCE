'''Challenge: 
Write a program that calculates the factorial of a given number.
Define a function called factorial that takes an integer as input and returns its factorial.
Call this function to compute the factorial of a number entered by the user'''

#find the factorial of a number
def findFactorial (num):
    factorial = num
    #for to loop through each number from num to 1
    for i in range(1,num-1):
        #multiply the result by the number - 1
        factorial = factorial*(num-i)
    return factorial
#take user input
number = int(input('enter a number: '))
print('the factorial of your number is: '+ str(findFactorial(number)))