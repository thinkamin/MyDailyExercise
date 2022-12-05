from collections import defaultdict
from heapq import *

def Prim(vertexs,edges,start_node):
    adjacent_vertex = defaultdict(list)
    for v1,v2,length in edges:
        adjacent_vertex[v1].append((length,v1,v2))
        adjacent_vertex[v2].append((length,v2,v1))
    print(adjacent_vertex)

    mst=[]
    closed=set(start_node)
    print("start_node",start_node)
    adjacent_vertex_edges=adjacent_vertex[start_node]
    heapify(adjacent_vertex_edges)
    print("adjacent_vertex_edges",adjacent_vertex_edges)
    while adjacent_vertex_edges:
        w,v1,v2=heappop(adjacent_vertex_edges)
        #这不就是深度优先的思路么
        if v2 not in closed:
            closed.add(v2)
            mst.append((v1,v2,w))

            for next_vertex in adjacent_vertex[v2]:
                if next_vertex[2] not in closed:
                    heappush(adjacent_vertex_edges,next_vertex)
    return mst
vertexs=list('ABCDEFG')
edges=[('A','B',7),
        ('A','D',5),
        ('B','C',8),
        ('B','D',9),
        ('B','E',7),
        ('C','E',5),
        ('D','E',15),
        ('D','F',6),
        ('E','F',8),
        ('F','G',11)]
print(Prim(vertexs,edges,'A'))

