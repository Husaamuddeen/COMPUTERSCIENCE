arrayQueue = [None,None,None,None,None]
front = 0 
rear = -1 
size = 0
maxSize = 5

def enQueue(item):
    global rear, size
    if isfull():
        print('The queue is full')
        return
    else:
        rear = (rear+1)%maxSize
        arrayQueue[rear] = item
        print('You have enqueued '+str(item))
        size = size + 1

def deQueue():
    global front, size
    if isEmpty():
        print('The queue is empty')
        return
    else:
        removedItem = arrayQueue[front]
        front = (front+1)%maxSize
        size = size - 1
        return removedItem

def isfull():
    if size == maxSize:
        return True
    else:
        return False

def isEmpty():
    if size == 0:
        return True
    else:
        return False

def menu():
    global finished
    print('Choose an operation\n1: add to the queue\n2: dequeue\n3: display the queue\n4: exit')
    choice = int(input('Enter 1 to 4: '))
    match choice:
        case 1:
            item = int(input('Enter the item you want to add to the queue: '))
            enQueue(item)
        case 2:
            removedItem = deQueue()
            print('You have dequeued '+str(removedItem))
        case 3:
            print(arrayQueue)
        case 4:
            print('Goodbye.')
            finished = True

finished = False
while not finished:
    menu()
