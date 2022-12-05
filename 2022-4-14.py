from my import gen_num
from collections import namedtuple
#from my import G1,G2
#from collections import deque
# num_lst = gen_num()
node = {}
rank ={}

def make_set(point):
    node[point]=point
    rank[point]=0

def find(point):
    if node[point]!=point:
        node[point]=find(node[point])
    return node[point]

def merge(point1,point2):
    root1=find(point1)
    root2=find(point2)
    if root1!=root2:
        if rank[root1]>rank[root2]:
            node[root2]=root1
        else:
            node[root1]=root2
            if rank[root1]==rank[root2]:
                rank[root2]+=1

def Kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    mst = set()
    edges=list(graph['edges'])
    edges.sort()
    for edge in edges:
        w,v1,v2=edge
        if find(v1)!=find(v2):
            merge(v1,v2)
            mst.add(edge)
    return mst

graph = {
        'vertices':list('ABCD'),
        'edges':set(
            [
            (1,'A','B'),
            (5,'A','C'),
            (3,'A','D'),
            (4,'B','C'),
            (2,'B','D'),
            (1,'C','D')
            ]
            )
        }
print(Kruskal(graph)) 
