class node:
    def __init__(self,data=None,next1=None):
        self.data= data
        self.next1= next1

a1 = node(0)
a2 = node(1)
a3 = node(2)
a4 = node(3)
a5 = node(4)

a1.next1=a2
a2.next1=a3
a3.next1=a4
a4.next1=a5
a5.next1=a2

def check(aFirst):
    if not aFirst:
        return False
    else:
        slow,fast=aFirst,aFirst
        while fast:
            if fast.next1.next1 and slow.next1:
                fast=fast.next1.next1
                slow=slow.next1
            if fast==slow:
                break
        fast = aFirst
        while fast!=slow:
            slow=slow.next1
            fast=fast.next1
    return fast
print(check(a1))
print(a1.next1)




