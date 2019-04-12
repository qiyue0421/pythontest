# 选择排序的关键在于——每次遍历列表进行排序时，找出最大值，遍历完成后执行交换操作，将最大值放到正确的位置
def selectSort(alist):
    # 遍历n-1次排序
    for fillsolt in range(len(alist)-1, 0, -1):
        position_max = 0
        # 遍历列表，这里从1开始的原因是，第一个元素赋值给了position_max
        for location in range(1, fillsolt+1):
            if alist[location] > alist[position_max]:
                # 总是将最大值存入position_max中
                position_max = location
        # 交换操作，将最大值放在正确位置
        alist[fillsolt], alist[position_max] = alist[position_max], alist[fillsolt]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectSort(alist)
print(alist)
