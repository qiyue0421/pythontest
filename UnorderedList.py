class Node:
    def __init__(self, initdata):
        # 节点的数据项
        self.data = initdata
        # 下一个节点的引用
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# 无序列表类
class UnorderedList:
    # 列表本身不包含节点项，只是维护一个指向链表头部节点的引用
    def __init__(self):
        # 提供入口点
        self.head = None

    def isEmpty(self):
        return self.head is None

    # 添加新节点的最简单方法就是在链表头部进行操作
    def add(self, item):
        # 新节点
        temp = Node(item)
        # 更改新节点的下一个引用，使其指向旧链表的第一个节点（self.head总是存储链表的头部节点）
        temp.setNext(self.head)
        # 修改self.head使其指向新节点（即链表的第一个节点）
        self.head = temp

    # 基于链表遍历
    def size(self):
        current = self.head
        count = 0
        # 如果没有遍历完成
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    # 基于链表遍历
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                # 移向下一个节点
                current = current.getNext()
        return found

    # 基于链表遍历
    def remove(self, item):
        # 总是指向当前元素（即要移除的元素）
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # 如果该元素是第一个元素，则直接将头节点指向current的下一个引用即可,current被删除
        if previous is None:
            self.head = current.getNext()
        # 不是第一个元素，调整两个外部引用，删除current
        else:
            previous.setNext(current.getNext())


list = UnorderedList()
list.add('99')
list.add('fafa')
print(list.size())
print(list.search('99'))
print(list.search('tt'))
list.remove('99')
print(list.size())
