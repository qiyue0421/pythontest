import time


def showtime(func):
    def count():
        starttime = time.time()
        func()
        time0 = time.time() - starttime
        print('函数a的运行时间为:' + str(time0))
    return count


@showtime
def a():
    return sum(range(1, 100000))


a()
