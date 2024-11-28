import ast
import random


def userVerify(user):
    users = open('users.txt','r')
    userID = input('please enter a 10 character ID: ')
    if len(userID) == 10:
        for line in users:
            account = ast.literal_eval(line)
            if userID == account[0]:
                print('ID verified.')
                user = account
                users.close()
                return user
    users.close()
    return user


def PINVerify(user):
    PIN = int(user[1])
    PINtry = input('please enter the 4 digit PIN: ')
    if PINtry.isnumeric():
        if PIN == int(PINtry): 
            print('PIN accepted')
            return 'success'
        else:
            print('incorrect PIN, access denied')
            return 'failed'
        

def password(user):
    count = 0
    correct = 0
    while count < 3:
        password = user[2]
        index = random.randint(0,len(password)-1)
        guess = input(f'enter the character in the position {index+1} of your password: ')
        if guess == password[index]:
            correct = correct + 1
        count = count + 1
    if correct == 3:
        return 'success'
    else:
        return 'failed'
            

user = 'unverified'
count = 0
while user == 'unverified' and count < 3:
    user = userVerify(user)
    if user == 'unverified':
        count = count + 1
    else:
        PINResult = PINVerify(user)
        if PINResult == 'failed':
            count = 3
        else:
            count = 0
            passwordCount = 0
            while passwordCount < 3:
                passwordCheck = password(user)
                if passwordCheck == 'success':
                    print('successfully logged in')
                    passwordCount = 3
                else:
                    print('password failed, try again')
                    passwordCount = passwordCount + 1
if user == 'unverified':
    print('unable to verify user ID, access denied')
