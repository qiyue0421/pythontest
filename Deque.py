class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# 回文检查
def huiwencheck(string):
    d = Deque()
    # 字符串入Deque
    for i in string:
        d.addRear(i)
    # 相等标志位
    Equal = True
    while d.size() > 1 and Equal:
        # 移除首项和尾项，进行对比，如果不相等，标志位变化
        if d.removeFront() != d.removeRear():
            Equal = False
    # 隐藏条件为：deque长度为0和1的情况都是回文
    return Equal


print(huiwencheck('maddam'))
print(huiwencheck('fgafgg'))
