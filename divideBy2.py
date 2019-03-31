# 十进制转为任意进制
from pythonds.basic.stack import Stack


def divideBy2(num):
    s = Stack()
    while num > 0:
        rem = num % 2
        s.push(rem)
        num = num // 2
    binString = ''
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString


def baseConverter(num, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while num > 0:
        rem = num % base
        s.push(rem)
        num = num // base
    newString = ''
    while not s.isEmpty():
        newString = newString + digits[s.pop()]
    return newString


print(divideBy2(42))
print(baseConverter(42, 16))
