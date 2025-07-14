#create the class for a node
class Node():
    def __init__(self,value,pointer):
        self.value = value 
        self.pointer = pointer

#create the class for the linked list
class LinkedList():
    def __init__(self,firstval):
        self.headPointer = Node(firstval,None)
        self.tailPointer = self.headPointer
        self.size = 1
        #method to add an item to the list
    def add(self,value):
        current = self.headPointer
        found = False
        #check if the list is empty
        if self.isEmpty():
            current = Node(value, None)
        #check if the item should be added at the start of the list
        elif current.value > value:
            self.headPointer = Node(value, self.headPointer)
        #traverse the list and find the position where the item should be added
        else:
            while not found:
                if current.pointer == None:
                    found = True
                    current.pointer = Node(value, None)
                    self.size = self.size + 1
                elif current.pointer.value > value:
                    current.pointer = Node(value,current.pointer)
                    found = True
                    self.size = self.size + 1
                else:
                    current = current.pointer
                    print('next')

    #method to delete an item from the list
    def delete(self,value):
        current = self.headPointer
        finished = False
        #check if the list is empty
        if self.isEmpty():
            print('the list is empty')
        #check if the first item is to be deleted
        elif current.value == value:
            self.headpointer = current.pointer
        #traverse the list to search for the item to be deleted
        else:
            while not finished:
                if current.pointer.value == None:
                    print('item not found in the list.')
                    finished = True
                elif current.pointer.value == value:
                    current.pointer = current.pointer.pointer
                    finished = True
                current = current.pointer

    #method to check if the list is empty
    def isEmpty(self):
        if self.headPointer.value == None:
            return True
        return False

    #method to traverse the list
    def printList(self):
        currentPointer = self.headPointer
        print('printing list')
        print(currentPointer.value)
        while currentPointer.pointer != None:
            currentPointer = currentPointer.pointer
            print(currentPointer.value)

linked = LinkedList(76)
linked.printList()
linked.add(141)
linked.printList()
linked.add(21)
linked.printList()
linked.delete(141)
linked.printList()