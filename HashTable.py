# map数据类型的实现
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # 简单余数法计算原始哈希值
    def hashfunction(self, key, size):
        return key % size

    # 计算新的哈希值（+1线性探测）
    def rehsah(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, data):
        # 获取原始哈希值
        hashvalue = self.hashfunction(key, len(self.slots))
        # 如果是空槽，则插入该键值对
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # 首先判断是否跟插入的键相同，相同则替换该键对应的值
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            # 不同的话，导致散列冲突，这里使用rehash函数解决散列冲突
            else:
                # 获取新的哈希值
                newhashvalue = self.rehsah(hashvalue, len(self.slots))
                # 注意，这里while循环设置了两个跳出循环的条件：
                # 1、不是空槽，槽内有等于key的值
                # 2、空槽
                while self.slots[newhashvalue] is not None and self.slots[newhashvalue] != key:
                    newhashvalue = self.rehsah(newhashvalue, len(self.slots))
                # 空槽，直接插入键值对
                if self.slots[newhashvalue] is None:
                    self.slots[newhashvalue] = key
                    self.data[newhashvalue] = data
                # 不是空槽，槽内有等于key的值，则data替换为新数据值
                else:
                    self.data[newhashvalue] = data

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        pos = startslot
        while self.slots[pos] is not None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                # 一直+1探测，定位下一个可能的位置
                pos = self.rehsah(pos, len(self.slots))
                # 遍历完列表，即用尽所有可能的槽，则停止
                if pos == startslot:
                    stop = True
        return data

    # 重载魔术方法，允许使用[]访问
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[54] = 'cat'
print(H.slots)
print(H.data)
