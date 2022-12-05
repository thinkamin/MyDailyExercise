from my import gen_num
from collections import namedtuple
from my import G1,G2
from collections import deque
# num_lst = gen_num()

G1 = G1()
def bfs(G,s):
    visited = set()
    queue = deque([s])
    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.add(u)

        else:
            continue
        for v in G[u]:
            if v not in visited:
                queue.append(v)
    return visited
print(bfs(G1,'A'))


def dfs(G,s):
    visited = set()
    queue = list([s])
    while queue:
        u = queue.pop()
        if u not in visited:
            visited.add(u)

        else:
            continue
        for v in G[u]:
            if v not in visited:
                queue.append(v)
    return visited
print(bfs(G1,'A'))


