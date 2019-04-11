# 希尔排序的实现，关键在于使用不同增量切分多个子列表，对子列表使用插入排序，


# 增量插入排序
def gapInsertionSort(alist, start, gap):
    # 对单个子列表进行插入排序
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        pos = i
        while pos >= gap and alist[pos-gap] > currentvalue:
            alist[pos] = alist[pos-gap]
            pos = pos - gap
        alist[pos] = currentvalue


# 希尔排序
def shellSort(alist):
    # 增量为4
    sublistcount = len(alist)//2
    while sublistcount > 0:
        # 分别对四个子列表进行插入排序
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print('After increment of size', sublistcount, 'The list is', alist)
        # 缩小增量，接着进行增量为2、增量为1的排序
        sublistcount = sublistcount // 2


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
