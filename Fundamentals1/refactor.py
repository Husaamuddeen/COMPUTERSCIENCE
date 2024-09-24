'''
Maintainability: Refactor	Given this piece of code that checks if a number is prime, refactor it to improve maintainability.
 Use meaningful variable names and break down the logic into smaller, well-named functions (e.g., is_prime, get_user_input).
 Add comments to explain the purpose of each function and block of code 
'''

def prime_check():
    num = int(input("Enter a number: "))
    #take user input for the number to check
    if num > 1:
    #if number is 
        factors = False
        #for loop which cycles through all numbers which can be factors of the number
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                print(num, "is not a prime number")   
                factors = True
                break
        if factors == False:
            print(num, "is a prime number") 
    else:
        print(num, "is not a prime number")
prime_check()