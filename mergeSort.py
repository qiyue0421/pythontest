# 归并排序的关键在于：拆分和合并操作
def mergeSort(alist):
    print('Spliting', alist)
    if len(alist) > 1:
        # 拆分操作
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # 递归算法，不断将列表拆分为一半
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # 合并操作
        i, j, k = [0]*3
        # 分别从左到右比较两个数组中的值，然后将较小的值放入新的数组（即alist[k])中，
        # 直到其中一个数组中的元素比较完毕，则退出循环
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        # 如果lefthalf中还有剩余元素
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        # 如果righthalf中还有剩余元素
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

    print('Merging', alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
