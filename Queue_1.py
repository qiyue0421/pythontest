import random
from pythonds.basic.queue import Queue


# 打印任务类
class Task:
    def __init__(self, time):
        # 时间戳，表示任务被创建并放置到打印机队列中的时间
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    # 打印任务等待打印的时间
    def waitTime(self, currenttime):
        return currenttime - self.timestamp


# 接受每分钟处理页数，以便计算所需时间
class Printer:
    def __init__(self, ppm):
        # 每分钟处理页数（打印机效率）
        self.pagerate = ppm
        # 打印机当前状态
        self.currentTask = None
        # 打印机打印当前任务所需时间
        self.timeRemaining = 0

    # 清空任务打印时间，直到打印机状态为空闲
    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    # 传入一个打印任务实例，模拟打印机启动打印
    def startNext(self, newtask):
        # 修改打印机状态为启动
        self.currentTask = newtask
        # 根据打印任务的页数，确定需要多少时间（单位：秒）
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


# 决定是否创建新的打印任务
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


# 参数：模拟时间(单位：秒） 每分钟处理页数
def simulation(numSeconds, pagesPerMinute):
    # 通过传入 每分钟处理页数（也就是打印机模式）作为参数，实例化一个Printer类
    labprinter = Printer(pagesPerMinute)

    # 实例化队列
    printQueue = Queue()

    # 任务的等待时间列表，用于计算平均等待时间
    waitingtimes = []

    # 总打印任务数量
    count = 0

    # 模拟时间中的每一秒
    for currentSecond in range(numSeconds):
        # 判断是否创建新的打印任务
        if newPrintTask():
            # 实例化打印任务类，传入时间戳
            task = Task(currentSecond)
            count += 1
            # 打印任务入队列
            printQueue.enqueue(task)

        # 如果打印机不忙，并且队列不为空（有任务在等待）
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            # 从队列中删除一个任务并将其分配给打印机
            nexttask = printQueue.dequeue()
            # 计算等待时间，附件到列表中稍后处理
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # 计算打印时间（根据打印任务的页数）
            labprinter.startNext(nexttask)

        # 打印需要一秒
        labprinter.tick()

    # 打印结束计算平均等待时间
    averagewait = sum(waitingtimes)/len(waitingtimes)

    print("共计模拟打印%3d个任务 平均每个任务等待%6.2f秒%3d个剩余任务" % (count, averagewait, printQueue.size()))


# 模拟10次，每次一小时，每分钟处理5页
for i in range(10):
    simulation(3600, 15)
