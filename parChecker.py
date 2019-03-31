from pythonds.basic.stack import Stack


def match(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('[{()}]'))
