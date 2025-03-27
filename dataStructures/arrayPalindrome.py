stack = ['','','','','','','','','','']
top = -1

#function to check if the stack is empty
def isEmpty():
    if top == -1:
        return True
    return False
    
#function to check if the stack is full
def isFull():
    if top == 9:
        return True
    return False

#function to push the item to the stack
def push(item):
    global top
    if isFull():
        print('stack overflow')
    else:
        stack[top+1] = item
        top = top + 1

#function to pop the top item from the stack
def pop():
    global top
    if isEmpty():
        print('stack underflow')
    else:
        top = top - 1
        return stack[top+1]

#loop to validate the user input to less than 10 characters
sized = False
while not sized:
    userword = input('enter the word to check if it is a palindrome: ')
    if len(userword) <= 10:
        sized = True
    else:
        print('must be less than 10 characters.')

#push the user input to the stack
for i in range(0,len(userword)):
    push(userword[i])

#pop the stack and compare with the user input
palindrome = True
for i in range(0,len(userword)):
    if pop() != userword[i]:
        palindrome = False

if palindrome:
    print('Palindrome')
else:
    print('not a palindrome')