class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            # 当前值大于插入值表示找到可以插入的位置了，修改停止标志位
            if current.getData() > item:
                stop = True
            # 继续下一次遍历
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData == item:
                found = True
            else:
                # 查找值大于搜索项则停止搜索
                if current.getData > item:
                    stop = True
                # 否则，继续移动
                else:
                    current = current.getNext()
        return found

    def pop(self, pos=None):
        current = self.head
        previous = None
        count = 0
        """if pos is None:
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            if previous is None:
                self.head = None
                return current.getData()
            else:
                previous.setNext(None)
                return current.getData()
        else:
            while count != pos and current.getNext() is not None:
                previous = current
                current = current.getNext()
                count += 1
            if previous is None:
                self.head = None
            else:
                previous.setNext(current.getNext)
            return current.getData()"""
        ps = False
        while current is not None and not ps:
            previous = current
            current = current.getNext()
            if pos is not None and count != pos:
                count += 1
                if count == pos:
                    ps = True
        if previous is None:
            self.head = None
        else:
            previous.setNext(current.getNext())
        return current.getData()

    def index(self, item):
        current = self.head
        count = 0
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                count += 1
                current = current.getNext()
        return count


order = OrderedList()
order.add(56)
order.add(30)
order.add(45)
order.add(16)
print(order.size())
print(order.index(16))
print(order.pop())

#print(order.pop())
#print(order.size())
print(order.pop(1))
# print(order.pop())
