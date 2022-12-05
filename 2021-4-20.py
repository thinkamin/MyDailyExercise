from G import G
from collections import deque
def bfs(G,s):
    explored = {s}
    queue =deque()
    queue.append(s)
    while queue:
        v = queue.popleft()
        for w in G[v]:
            if w not in explored:
                queue.append(w)
                explored.add(w)
    return explored
print(bfs(G,'A'))

    
