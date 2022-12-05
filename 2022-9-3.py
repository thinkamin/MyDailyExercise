from my import gen_num
from collections import namedtuple
from my import G1,G2
from collections import deque
num_lst = gen_num()
print(num_lst)
G1 = G1()
print(G1)

def bfs(G,s):
    queue = deque([s])
    visited = set()
    while queue:
        u = queue.popleft()
        print(u)
        if u not in visited:
            visited.add(u)
        for v in G[u]:
            print(v)
            if v not in visited:
                queue.append(v)
    return visited
print(bfs(G1,'A'))

def dfs(G,s):
    queue = [s]
    visited = set()
    while queue:
        u = queue.pop()
        if u not in visited:
            visited.add(u)
        for v in G[u]:
            if v not in visited:
                queue.append(v)
    return visited
print(dfs(G1,'A'))

