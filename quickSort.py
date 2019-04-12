# 快速排序的实现，关键在于根据设定的枢轴值找到分隔点，再根据分隔点进行分区递归操作


# 找寻分隔点函数
def partition(alist, first, last):
    # 枢轴值
    pivotvalue = alist[first]

    # 左右标记位
    leftmark = first + 1
    rightmark = last

    # 分隔完成符
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            # 左标记递增
            leftmark += 1

        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            # 右标记递减
            rightmark -= 1

        # 如果右标记小于左标记，说明分隔点已经找到,此时分隔点就是右标记
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    # 找到了分隔点，将枢轴值放入分隔点内
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    # 需要返回分隔点以执行后面的递归操作
    return rightmark


# 分区递归函数：根据分隔点不断递归调用快速排序
def quickSortHelper(alist, first, last):
    # 递归的退出条件：列表中只有一个元素就不需要排序
    if first < last:
        # 分隔点
        splitpoint = partition(alist, first, last)

        # 根据分隔点进行递归操作
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
