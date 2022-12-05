from G import G,printG
# printG()
from collections import deque
def bfs(G,s):
    '''
    G:graph
    s:source
    '''
    queue = deque([s])
    explored = set()
    while queue:
        v = queue.popleft()
        explored.add(v)
        for i in G[v]:
            if i not in explored:
                queue.append(i)
                print(i)
    return explored
print(bfs(G,'A'))



