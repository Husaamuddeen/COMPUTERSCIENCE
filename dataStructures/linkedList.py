class Node():
    def __init__(self,value,pointer):
        self.value = value 
        self.pointer = pointer

class LinkedList():
    def __init__(self,firstval):
        self.headPointer = Node(firstval,None)
        self.tailPointer = self.headPointer
        self.size = 1
    def add(self,value):
        current = self.headPointer
        found = False
        if current.value == None:
            current = Node(value, None)
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

    def delete(self,value):
        current = self.headPointer
        found = False
        if self.isEmpty():
            print('the list is empty')
        else:
            while not found:
                if current.pointer.value == None:
                    print('item not found in the list.')
                elif current.pointer.value == value:
                    current.pointer = current.pointer.pointer
    def isEmpty(self):
        if self.headPointer.value == None:
            return True
        return False

    def printList(self):
        currentPointer = self.headPointer
        print('printing list')
        print(currentPointer.value)
        for i in range(1,self.size):
            currentPointer = currentPointer.pointer
            print(currentPointer.value)

linked = LinkedList(76)
linked.printList()
linked.add(141)
linked.printList()
linked.add(21)
linked.printList()
linked.delete(141)