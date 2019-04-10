def bubbleSort(alist):
    # 如果有n个项，则需要比较n-1次
    for passnum in range(len(alist)-1, 0, -1):
        # 开始遍历列表
        for i in range(passnum):
            # 每次比较一对
            if alist[i] > alist[i+1]:
                # 交换操作
                alist[i], alist[i+1] = alist[i+1], alist[i]


# 短冒泡排序
def shortBubbleSort(alist):
    exchange = True
    passsum = len(alist) - 1
    while passsum > 0 and exchange:
        # 设置交换标志位为False，如果在遍历过程中没有发生交换，则停止排序
        exchange = False
        # 遍历列表，检查是否需要交换
        for i in range(passsum):
            if alist[i] > alist[i+1]:
                # 需要交换，将标志位置True
                exchange = True
                # 交换操作
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passsum = passsum - 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)
