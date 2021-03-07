class BinaryTree:
    def __init__(self, rootVal):
        self.key = rootVal
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(tree):
        if tree != None:
            postorder(tree.getLeftChild())
            postorder(tree.getRightChild())
            print(tree.getRootVal())


t = BinaryTree('a')
t.insertRight('c')
t.insertLeft('b')
(t.getLeftChild()).insertLeft('d')
(t.getLeftChild()).insertLeft('e')
(t.getLeftChild()).insertLeft('f')

t.preorder()




