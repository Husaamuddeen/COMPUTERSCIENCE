class Node():
    def __init__(self,InValue):
        self.value = InValue
        self.left = None
        self.right = None

class Tree():
    def __init__(self,firstVal):
        self.root = Node(firstVal)
    
    def add(self,InValue):
        current = self.root
        found = False
        while not found:
            if current.value > InValue:
                if current.left == None:
                    current.left = Node(InValue)
                    found = True
            if current.value < InValue:
                if current.right == None:
                    current.right = Node(InValue)
                    found = True

    def preOrder(self,position):
        print(position.value)
        if position.left != None:
            self.preOrder(position.left)
        if position.right != None:
            self.preOrder(position.right)

    def inOrder(self,position):
        if position.left != None:
            self.preOrder(position.left)
        print(position.value)
        if position.right != None:
            self.preOrder(position.right)

    def postOrder(self,position):
        if position.left != None:
            self.preOrder(position.left)
        if position.right != None:
            self.preOrder(position.right)
        print(position.value)

myTree = Tree(2)
myTree.add(1)
myTree.add(3)
myTree.preOrder(myTree.root)
myTree.inOrder(myTree.root)
myTree.postOrder(myTree.root)