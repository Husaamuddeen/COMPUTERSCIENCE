#an array is a mutable structure which can hold multiple elemnts of data, the size of the array can be changed by appending and popping
#a list is an immutable structure which can hold multiple elements of data, and the size of the list cannot be changed and is defined when the list is instantiated

def getCount():
    valid = False
    while not valid:
        count = int(input("enter a number between 1 and 3: "))
        if count > 0 and count < 4:
            valid = True
    return count

def getNumbers(count,number):
    if count == 1:
        print(str(number+1))
    elif count == 2:
        print(str(number+1)+", "+str(number+2))
    elif count == 3:
        print(str(number+1)+", "+str(number+2)+", "+str(number+3))
    number = number + count
    return number

number = 0
finished = False

while not finished:
    print("")
    print("player 1 turn")
    count = getCount()
    number = getNumbers(count,number)
    if number > 14:
        print("player 2 wins")
        finished = True
    else:
        print("")
        print("player 2 turn")
        count = getCount()
        number = getNumbers(count,number)
        if number > 14:
            print("player 1 wins")
            finished = True