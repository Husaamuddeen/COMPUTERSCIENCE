import ast
import random
def userVerify():
    verified = False
    users = open('users.txt','r')
    userID = input('please enter a 10 character ID: ')
    if len(userID) == 10:
        print('a')
        for line in users:
            account = ast.literal_eval(line)
            if userID == account[0]:
                print('verified')
                verified = True
                user = account
                users.close()
                return user
    users.close()
    return verified
def PINVerify():
    PIN = int(user[1])
    PINtry = input('please enter the 4 digit PIN: ')
    if PINtry.isnumeric():
        if PIN == int(PINtry): 
            print('PIN accepted')
            for i in range(3):
                password = user[2]
                index = random.randint(0,len(password)-1)
                guess = input(f'enter the character in the position {} of your password')
                if guess == password[index]:
                    print('correct')
        else:
            print('incorrect PIN, access denied')
            count = 3
def login():
    verified = False
    count = 0
    users = open('users.txt','r')
    while verified != True and count < 3:
        userID = input('please enter a 10 character ID: ')
        if len(userID) == 10:
            print('a')
            for line in users:
                account = ast.literal_eval(line)
                if userID == account[0]:
                    print('verified')
                    verified = True
                    user = account
            print(verified)
            if verified == False:
                print('your ID does not exist.')
                count = count + 1
            else:
                PIN = int(user[1])
                PINtry = input('please enter the 4 digit PIN: ')
                if PINtry.isnumeric():
                    if PIN == int(PINtry): 
                        print('PIN accepted')
                        for i in range(3):
                            password = user[2]
                            index = random.randint(0,len(password)-1)
                            guess = input(f'enter the character in the position {} of your password')
                            if guess == password[index]:
                                print('correct')
                    else:
                        print('incorrect PIN, access denied')
                        count = 3
                        
        else:
            print('your input was not 10 characters.')
            count = count + 1
    users.close()

user = False
count = 0
while user == False and count < 3:
    user = userVerify()
    if user == False:
        count = count + 1
    else:
        PIN = int(user[1])
        PINtry = input('please enter the 4 digit PIN: ')
        if PINtry.isnumeric():
            if PIN == int(PINtry): 
                print('PIN accepted')
                for i in range(3):
                    password = user[2]
                    index = random.randint(0,len(password)-1)
                    guess = input(f'enter the character in the position {} of your password')
                    if guess == password[index]:
                        print('correct')
            else:
                print('incorrect PIN, access denied')
                count = 3



