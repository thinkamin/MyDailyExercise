from G import G
from collections import deque
print(G)

def dfs(G,s):
    visited = set()
    queue = deque([s]) 
    while queue:
        u = queue.pop()
        if u in visited:
            continue
        else:
            visited.add(u)
        for v in G[u]:
            queue.append(v)
    return visited
print(dfs(G,'A'))

