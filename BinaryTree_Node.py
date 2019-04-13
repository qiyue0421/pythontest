# 节点实现树数据结构
class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
print(r.getRightChild())

r.insertLeftChild('b')
r.insertRightChild('c')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
print(r.getRightChild())
print(r.getRightChild().getRootVal())

r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
