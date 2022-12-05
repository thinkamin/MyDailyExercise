from G import G,printG
# print(G)
from collections import deque
printG()

def bfs(G,s):
    explored = set(s)
    queue =deque(s)
    while queue:
        #从头出保证了广度优先
        v = queue.popleft()
        for w in G[v]:
            if w not in explored:
                explored.add(w)
                print(w)
                queue.append(w)
    '''
    无序输出
    '''
    return explored

print(bfs(G,'A'))
