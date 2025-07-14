letterTree = [
    [1,'M',2],
    [3,'H',4],
    [5,'T',6],
    [-1,'D',-1],
    [-1,'K',-1],
    [-1,'R',-1],
    [-1,'X',-1]
]

def inOrder(node):
    if letterTree[node][0] != -1:
        inOrder(letterTree[node][0])
    print(letterTree[node][1],end=' ')
    if letterTree[node][2] != -1:
        inOrder(letterTree[node][2])

def preOrder(node):
    print(letterTree[node][1],end=' ')
    if letterTree[node][0] != -1:
        inOrder(letterTree[node][0])
    if letterTree[node][2] != -1:
        inOrder(letterTree[node][2])

def preOrder(node):
    if letterTree[node][0] != -1:
        inOrder(letterTree[node][0])
    if letterTree[node][2] != -1:
        inOrder(letterTree[node][2])
    print(letterTree[node][1],end=' ')

def menu():
    print('to traverse the list in pre-order, enter 1')
    print('to traverse the list in order, enter 2')
    print('to traverse the list in post-order, enter 3')
    choice = int(input('--: '))
    match choice:
        case 1:
            preOrder(0)
        case 2:
            inOrder(0)
        case 3:
            postOrder(0)

menu()