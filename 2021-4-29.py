from G import G,printG
from collections import deque
# printG()
def bfs(G,s):
    visited=set()
    queue = deque([s])
    while queue:
        u = queue.popleft()
        visited.add(u)
        # print(u)
        for v in G[u]:
            if v not in visited:
                queue.append(v)
    return visited
print(bfs(G,'A'))

