# 递归绘制简单分形树
import turtle


def tree(branchlen, t):
    if branchlen > 5:
        # 向画笔当前方向移动branchlen距离
        t.forward(branchlen)
        # 右转20度
        t.right(20)
        # 绘制右树
        tree(branchlen-15, t)
        # 左转40度
        t.left(40)
        # 绘制左树
        tree(branchlen-15, t)
        # 右转20度，此时相对角度为水平线为90度
        t.right(20)
        # 向画笔相反方向移动branchlen距离
        t.backward(branchlen)


if __name__ == '__main__':
    t = turtle.Turtle()
    mywin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    t.speed(1)
    tree(100, t)
    mywin.exitonclick()
