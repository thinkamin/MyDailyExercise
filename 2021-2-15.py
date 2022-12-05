#deep first search
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

class Vertex:
    def __init__(self,name,color='white',neighbor=None,d=-1,f=-1,pred=-1):
        
        '''
        args:
        d:discover
        f:finish
        pred:前驱
        '''
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

counter = 0    

def dfs_visit(source):
    source.color='Gray'
    global counter
    counter +=1
    source.d=counter
    # print(counter)
    for v in source.neighbor:
        if v.color=='white':
            v.pred=source
            dfs_visit(v)
    source.color='Black'
    counter +=1
    source.f=counter

dfs_visit(Vertex_list[0])

for v in Vertex_list:
    if v.color=='white':
        dfs_visit(v)

for v in Vertex_list:
    print('name',v.name)
    print('color',v.color)
    print('d',v.d)
    print('f',v.f)
    print('pred',v.pred)
    print('***')



