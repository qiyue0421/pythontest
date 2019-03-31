from pythonds.basic.stack import Stack


def infixtopostfix(infixexpr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    s = Stack()
    postfixlist = []
    tokenlist = list(infixexpr)
    # 从左到右遍历中缀表达式
    for token in tokenlist:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixlist.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            tokentop = s.pop()
            while tokentop != '(':
                postfixlist.append(tokentop)
                tokentop = s.pop()
        # 操作符
        else:
            # 比较栈顶部的操作符，如果顶部操作符优先级高，则弹出顶部操作符
            while (not s.isEmpty()) and prec[s.peek()] >= prec[token]:
                postfixlist.append(s.pop())
            # 否则，操作符接着入栈
            s.push(token)
    # 遍历完所有表达式后，将栈内剩余操作符出栈
    while not s.isEmpty():
        postfixlist.append(s.pop())
    return ''.join(postfixlist)


print(infixtopostfix('A*B+C*D'))
print(infixtopostfix('(A+B)*C-(D-E)*(F+G)'))


def domath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 /op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2


def countpostfix(postfixeper):
    postfixlist = list(postfixeper)
    s = Stack()
    for post in postfixlist:
        if post in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or post in '0123456789':
            s.push(int(post))
        else:
            op2 = s.pop()
            op1 = s.pop()
            result = domath(post, op1, op2)
            s.push(result)
    return s.pop()
