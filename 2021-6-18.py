#import  gen_num
from G import G,printG
from collections import deque
# printG()

def dfs(G,s):
    queue = list([s]) 
    visited = set()
    while queue:
        u = queue.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in G[u]:
            queue.append(v)
    print(visited)
    return visited
print(dfs(G,'A'))

