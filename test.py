import ast
users = open('users.txt','r')
for line in users:
    print(line)
    print('a')
    user = ast.literal_eval(line)
    print(user)
    print(user[0])