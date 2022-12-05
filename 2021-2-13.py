#bread first search
#定义图
import collections

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

class Vertex:
    def __init__(self,name,color='white',neighbor=None,d=-1,f=-1,pred=-1):
        self.name=name
        self.color=color
        self.neighbor=neighbor
        self.d=d
        self.f=f
        self.pred=pred

Vertex_list = []
for v in G.keys():
    nodename = Vertex(name=str(v),color='white',neighbor=None,d=-1,f=-1,pred=-1)
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

Q = collections.deque()
Q.append(Vertex_list[0])
while len(Q)!=0:
    u = Q[0]
    for neighbor in u.neighbor:
        if neighbor.color =='white':
            neighbor.pred = u
            neighbor.color = 'Gray'
            Q.append(neighbor)
            print(Q)
    Q.popleft()
    u.color =  'Black'

