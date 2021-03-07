# implementation of 'map' ADT (other two are binary search on a list and hash tables)
# BST property: keys < parent to the left and keys > parent to the right
# num nodes at level n = 2^n; height of tree with n nodes = log(n)
# total num nodes in completely balanced bin tree = 2^(h+1)-1 (h = height)
# put could be O(n) if keys inserted in sorted manner; can use AVL tree (since it's self-balancing)
# remember you always need to update two sets of pointers (node to parent and parent to node) + remember to keep track of left/right esp. for parent -> node

class TreeNode:
    def __init__(self,key,val,left=None,right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                # AVL Tree
                # self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                # self.updateBalance(currentNode.rightChild)

    # def updateBalance(self, node):
    #     if node.BalanceFactor > 1 or node.balanceFactor < -1:
    #         self.rebalance(node)
    #         return
    #     if node.parent != None:
    #         if node.isLeftChild():
    #             node.parent.balanceFactor += 1
    #         elif node.isRightChild():
    #             node.parent.balanceFactor -= 1
    #         if node.parent.balanceFactor != 0:
    #             self.updateBalance(node.parent)

    # handling edge cases
    # If a subtree needs a left rotation to bring it into balance, first check the balance factor of the right child. If the right child is left heavy then do a right rotation on right child, followed by the original left rotation.
    # def rebalance(self,node):
    #     if node.balanceFactor < 0:
    #         if node.rightChild.balanceFactor > 0:
    #             self.rotateRight(node.rightChild)
    #             self.rotateLeft(node)
    #         else:
    #             self.rotateLeft(node)
    #     elif node.balanceFactor > 0:
    #         if node.leftChild.balanceFactor < 0:
    #             self.rotateLeft(node.leftChild)
    #             self.rotateRight(node)
    #         else:
    #             self.rotateRight(node)

    # def rotateLeft(self,rotRoot):
    #     newRoot = rotRoot.rightChild
    #     rotRoot.rightChild = newRoot.leftChild
    #     if newRoot.leftChild != None:
    #         newRoot.leftChild.parent = rotRoot
    #     newRoot.parent = rotRoot.parent
    #     if rotRoot.isRoot():
    #         self.root = newRoot
    #     else:
    #         if rotRoot.isLeftChild():
    #             rotRoot.parent.leftChild = newRoot
    #         else:
    #             rotRoot.parent.rightChild = newRoot
    #     newRoot.leftChild = rotRoot
    #     rotRoot.parent = newRoot
    # Derivation from writing balanceFactors of all nodes out and doing some algebra (since height of lower subtrees remains the same)
    #     rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
    #     newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)

    def remove(self, currentNode):
        # no children
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        # two children
        # succ is min value in subtree (guaranteed to have no more than 1 children)
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        # one child
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])


# AVL Trees
# keep track of a balance factor for each node in the tree
# balanceFactor = height(leftSubTree) - height(rightSubTree)
# subtree is left-heavy if balanceFactor > 0 else right-heavy
# [-1, 0, 1] considered balanced range
# AVL Trees worst case shown to be 1.44 * O(log(n)) (derivation uses Fibonacci and golden ratio)
# Rotations
# If a subtree needs a left rotation to bring it into balance, first check the balance factor of the right child. If the right child is left heavy then do a right rotation on right child, followed by the original left rotation.
# If a subtree needs a right rotation to bring it into balance, first check the balance factor of the left child. If the left child is right heavy then do a left rotation on the left child, followed by the original right rotation.



































