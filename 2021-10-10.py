import turtle as tt

def fac(n):
    if n<=1:
        return n
    else:
        return fac(n-1)+fac(n-2)
# print(fac(10))


def drawbranch(n,length,angel,miu):
    tt.pendown()
    tt.forward(length)
    if n>0:
        tt.right(angel)
        drawbranch(n-1,length*miu,angel,miu)
        tt.left(angel*2)
        drawbranch(n-1,length*miu,angel,miu)
    else:
        tt.right(90)
        tt.circle(3)
        tt.left(90)
        t=tt.heading()
        sethe
tt.left(90)
length=100
tt.forward(length)        
drawbranch(5,50,10,.8)

