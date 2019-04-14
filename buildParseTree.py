# 分析树生成器
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


def buildParseTree(fpexp):
    # 分解表达式
    fplist = fpexp.split()
    # 创建空栈用于跟踪父节点
    pStack = Stack()
    # 初始化一棵树
    eTree = BinaryTree('')
    # 入栈当前节点，因为后续操作要下降到子节点
    pStack.push(eTree)
    # 当前节点
    currentTree = eTree
    for i in fplist:
        if i == '(':
            # 创建左子节点
            currentTree.insertLeft('')
            # 入栈当前节点
            pStack.push(currentTree)
            # 下降到左子节点
            currentTree = currentTree.getLeftChild()
        # 如果是操作数，将当前节点的根值设为操作数，并返回父节点
        elif i not in ['+', '-', '/', '*', ')']:
            currentTree.setRootVal(int(i))
            # 出栈，返回到父节点
            parent = pStack.pop()
            # 当前节点为父节点
            currentTree = parent
        # 如果是操作符，则将当前节点的根植设为操作符，创建右节点
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            # 创建右子节点
            currentTree.insertRight('')
            # 入栈当前节点
            pStack.push(currentTree)
            # 下降到右子节点
            currentTree = currentTree.getRightChild()
        # 如果是 ） 符号，回到父节点
        elif i == ')':
            # 当前节点从子节点返回到父节点
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree
