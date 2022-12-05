from G import G,printG
from collections import deque
# printG()

def bfs(G,s):
    queue = deque([s])
    visited = set()
    while queue:
        u = queue.popleft()
        if u in visited:
            continue
        else:
            visited.add(u)
        for v in G[u]:
            if v in visited:
                continue
            else:
                queue.append(v)
    return visited
print(bfs(G,'A'))


