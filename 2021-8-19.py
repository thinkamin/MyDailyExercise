from G import G,printG
printG()
from collections import deque

def bfs(G,s):
    queue = deque([s])
    visited = set()
    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.add(u)
        for v in G[u]:
            if v in visited:
                continue
            else:
                queue.append(v)
                print(queue,visited)
    return visited
print(bfs(G,'A'))

def dfs(G,s):
    queue = list([s])
    visited =set()
    while queue:
        u = queue.pop()
        if u not in visited:
            visited.add(u)
        for v in G[u]:
            if v in visited:
                continue
            else:
                queue.append(v)
    return visited
print(dfs(G,'A'))
