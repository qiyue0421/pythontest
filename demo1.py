def digit(n, k):
    list = []
    for i in range(n):
        if str(k) in str(i):
            list.append(str(i))
    return len(list), list


count, list = digit(100, 2)
print("符合条件的有{0}个，分别是：{1}".format(count, list))
