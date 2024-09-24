import ast
def login():
    verified = False
    count = 0
    users = open('users.txt','r')
    while verified != True and count < 3:
        userID = input('please enter a 10 character ID: ')
        if len(userID) == 10:
            for line in users:
                account = ast.literal_eval(line)
                if userID = account[0]:
                    verfied = True
                    user = account
                    users.close()
            if verified == False:
                print('your ID does not exist.')
                count = count + 1
            else:
                PIN = int(user[1])
                PINtry = input('please enter the 4 digit PIN for the user ',user[0])
                if PINtry.isnumeric():
                    if PIN == PINtry: 
                        print('PIN accepted')
                        
        else:
            print('your input was not 10 characters.')
            count = count + 1


login()
