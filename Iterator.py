class Count:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
        return result


c = Count(101, 109)
print(next(c))
print()
for i in c:
    print(i)
