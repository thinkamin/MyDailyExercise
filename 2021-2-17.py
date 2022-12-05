#bread first search
'''
广度优先不能遍历到孤立节点
'''
#定义图
G = {
    's':['1','4'],
    '1':['s','2'],
    '2':['1','6','3'],
    '3':['2','4'],
    '4':['5','s','3'],
    '5':['4'],
    '6':['2'],
    '7':['8'],
    '8':['7']
        }
from collections import deque

class Vertex:
    def __init__(self,name,color='white',neighbor=None,dist=100,pred=-1):
        
        '''
        args:
        dist:distance
        pred:前驱
        '''
        self.name=name
        self.color=color
        self.neighbor=neighbor
        self.dist=100
        self.pred=pred

Vertex_list = []
for v in G.keys():
    nodename = Vertex(name=str(v),color='white',neighbor=None,dist=100,pred=-1)
    Vertex_list.append(nodename)
'''
G = {
    '0':['1','4'],
    '1':['0','2'],
    '2':['1','6','3'],
    '3':['2','4'],
    '4':['5','0','3'],
    '5':['4'],
    '6':['2'],
    '7':['8'],
    '8':['7']
        }

'''
Vertex_list[0].neighbor=[Vertex_list[1],Vertex_list[4]]
Vertex_list[1].neighbor=[Vertex_list[0],Vertex_list[2]]
Vertex_list[2].neighbor=[Vertex_list[1],Vertex_list[3],Vertex_list[6]]
Vertex_list[3].neighbor=[Vertex_list[2],Vertex_list[4]]
Vertex_list[4].neighbor=[Vertex_list[5],Vertex_list[0],Vertex_list[3]]
Vertex_list[5].neighbor=[Vertex_list[4]]
Vertex_list[6].neighbor=[Vertex_list[2]]
Vertex_list[7].neighbor=[Vertex_list[8]]
Vertex_list[8].neighbor=[Vertex_list[7]]

def bfs_visit(source):
    source.color='Gray'
    source.dist = 0
    Q = deque()
    Q.append(source)
    while len(Q)>0:
        u = Q[0]
        print(Q)
        # print(u.name)
        for v in u.neighbor:
            if v.color=='white':
                v.pred=u
                v.dist = u.dist+1
                v.color = "Gray"
                Q.append(v)
                # print(Q)
        Q.popleft()
        u.color='black'
bfs_visit(Vertex_list[0])
for v in Vertex_list:
    print('name',v.name)
    print('color',v.color)
    print('d',v.dist)
    print('pred',v.pred)
    print('***')



