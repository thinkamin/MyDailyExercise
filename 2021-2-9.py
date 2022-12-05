#data struct 
#stack
stack = []

#graph
#1 {1:[2,3],2:[1],3[]}
#2 [[0,1,1],
    [1,0,0],
    [0,0,0]]

#queue
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.item == []
    def enqueue(self,item):
        self.items.insert(0,item)#始终把最后一个放到最前面
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


