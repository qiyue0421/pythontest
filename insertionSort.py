# 插入排序的实现，关键在于将比较项插入到正确位置
def insertionSort(alist):
    # 需要遍历n-1次
    for index in range(1, len(alist)):
        # 将比较项保存
        currentvalue = alist[index]
        pos = index
        # 子列表的项大于比较项
        while pos > 0 and alist[pos-1] > currentvalue:
            # 将子列表中较大的项向右移动
            alist[pos] = alist[pos-1]
            pos -= 1
        # 将比较项插入到正确位置
        alist[pos] = currentvalue
