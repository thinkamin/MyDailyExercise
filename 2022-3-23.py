# from my import gen_num
# from collections import namedtuple
from my import G1,G2
from collections import deque
# num_lst = gen_num()
G1 = G1()
def bfs(G,start):
    visited = set()
    queue=deque([start])
    while queue:
        i = queue.popleft()
        if i not in visited:
            visited.add(i)
        for j in G[i]:
            if j not in visited:
                queue.append(j)
            else:
                continue
    return visited
print(bfs(G1,'A'))
def dfs(G,start):
    visited = set()
    queue=deque([start])
    while queue:
        i = queue.pop()
        if i not in visited:
            visited.add(i)
        for j in G[i]:
            if j not in visited:
                queue.append(j)
            else:
                continue
    return visited
print(dfs(G1,'A'))
