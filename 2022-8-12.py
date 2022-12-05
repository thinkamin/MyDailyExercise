from my import gen_num
from collections import namedtuple
from my import G1,G2
from collections import deque
# num_lst = gen_num()

G1 =G1()
print(G1)

def bfs(G,s):
    visited = list()
    queue = deque([s])
    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.append(u)

        for v in G[u]:
            if v not in visited:
                queue.append(v)
            else:
                continue
        print(visited)
    return visited
# print(bfs(G1,'A'))

def dfs(G,s):
    visited = list()
    queue = list([s])
    while queue:
        u = queue.pop()
        if u not in visited:
            visited.append(u)

        for v in G[u]:
            if v not in visited:
                queue.append(v)
            else:
                continue
        print(visited)
    return visited

print(dfs(G1,'A'))
