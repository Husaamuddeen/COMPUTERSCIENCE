#initialise linked list
linkedList = [
    ['Altaf',2],
    ['Mariam',6],
    ['Eesa',3],
    ['Husaam',5],
    ['Sam',None],
    ['Kaya',1],
    ['Rezwan',4],
    [None,None],
    [None,None]
]
start = 0
nextfree = 7
print(linkedList)
#function to traverse and print the linked list
def traverse():
    current = start
    print(linkedList[current][0])
    while linkedList[current][1] != None:
        current = linkedList[current][1]
        print(linkedList[current][0])

traverse()
print()
def add(value):
    global nextfree
    positioned = False
    current = start
    linkedList[nextfree][0] = value
    while linkedList[current][1] != None and not positioned:
        next = linkedList[current][1]
        if value > linkedList[next][0]:
            linkedList[nextfree][0] = linkedList[current][1]
            linkedList[current][1] = nextfree
            positioned = True
        current = linkedList[current][1]
        print(linkedList[current][0])
    nextfree = nextfree + 1
    print()

add('David')
traverse()