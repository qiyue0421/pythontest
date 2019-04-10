# 二分法查找
def binary_search(alist, item):
    first, last = 0, len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# 二分法查找递归版本
def binary_recursion(alist, item):
    # 设置第一个退出条件
    if len(alist) == 0:
        return False
    else:
        # 中间项
        midpoint = len(alist)//2
        # 设置第二个退出条件
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                # 使用切片创建左半部分，再次调用递归
                return binary_recursion(alist[:midpoint], item)
            else:
                # 使用切片创建右半部分，再次调用递归
                return binary_recursion(alist[midpoint+1:], item)


alist = [1, 12, 23, 34, 56, 67, 73, 82, 99]
print(binary_search(alist, 67))
print(binary_recursion(alist, 67))
