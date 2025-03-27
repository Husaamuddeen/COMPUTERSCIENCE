#take user input
myString = input('Please enter a word or phrase to be tested: ')
#push the list onto a stack
list1 = list(myString.lower())
numChars = len(list1)
s = []
for i in range(0,numChars):
    s.append(list1[i])
reverse = []
#pop each item in the stack and push them onto another stack
for i in range(0,len(list1)):
    reverse.append(s.pop())
#check if the original and final stacks are the same
if list1 == reverse:
    print('Palindrome')
else:
    print('Not a palindrome')