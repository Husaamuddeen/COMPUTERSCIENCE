#create a class for a node
class Node():
    def __init__(self,dataIn,PointerIn):
        self.data = dataIn
        self.pointer = PointerIn

#create a class for a stack data structure
class Stack():
    def __init__(self,dataIn):
        self.top = Node(dataIn,None)

    #method to push an item on to the stack
    def push(self, dataIn):
        self.top = Node(dataIn,self.top)

    #method to pop an item off the top of the stack
    def pop(self):
        pop = self.top.data
        self.top = self.top.pointer
        return pop
    
    #method to check if the stack is empty
    def isEmpty(self):
        if self.top == None:
            return True
        return False
    
word = input('Enter a word to check if it is a palindrome: ')
#push the given word on to a stack
wordStack = Stack(word[0])
for i in range(1,len(word)):
    wordStack.push(word[i])
palindrome = True
#pop from the stack and check values against the list
for i in range(0,len(word)):
    if wordStack.pop() != word[i]:
        palindrome = False

if palindrome:
    print('the word is a palindrome')
else:
    print('the word is not a palindrome')
