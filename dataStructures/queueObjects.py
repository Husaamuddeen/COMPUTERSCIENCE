class Node():
    def __init__(self,value,):
        self.value = value 
        self.next = None

class Queue():
    def __init__(self,firstVal,maxSize):
        self.frontPointer = Node(firstVal)
        self.rearPointer = self.frontPointer
        self.size = 1
        self.maxSize = maxSize

    def enQueue(self,value):
        if self.size == self.maxSize:
            print('The queue is full try next time')
        else:
            self.rearPointer.next = Node(value)
            self.rearPointer = self.rearPointer.next
            self.size = self.size + 1

    def deQueue(self):
        if self.size == 0:
            print('The queue is empty')
        else:
            self.frontPointer = self.frontPointer.next
            self.size = self.size - 1

    def printQueue(self):
        print("The Queue:")
        location = self.frontPointer
        for i in range(0,self.size):
            print(location.value)
            location = location.next
        print('End')
        print(' ')


busQ = Queue(141,5)
busQ.enQueue(21)
busQ.printQueue()
busQ.enQueue(76)
busQ.printQueue()
busQ.deQueue()
busQ.printQueue()