from G import G,printG
from collections import deque

# printG()
print(G)
def bfs(G,s):
    visited=set()
    queue=deque([s])
    while queue:
        u = queue.popleft()
        if u in visited:
            continue
        visited.add(u)
        for v in G[u]:
            if v in visited:
                continue
            queue.append(v)
    return visited
print(bfs(G,'A'))
    
