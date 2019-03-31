# 队列类
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # 假定队尾在列表中的位置为0（列表的最后一个元素）
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.isEmpty())
q.enqueue('4')
q.enqueue('True')
q.enqueue('8.4')
print(q.size())
print(q.isEmpty())
print(q.dequeue())
print(q.items)
print(q.size())


# 模拟烫手山芋过程
def hotPotato(namelist, num):
    q = Queue()
    # 名称列表入队列
    for name in namelist:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    # 返回最后一个
    return q.dequeue()


namelist = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
print(hotPotato(namelist, 7))
