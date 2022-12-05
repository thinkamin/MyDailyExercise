from my import gen_num,G1,G2
from collections import deque
import heapq

g1 = G1()
g2 = G2()
print(g2)

def bfs(G,s):
    explored = []
    queue = deque([s])
    while queue:
        u = queue.popleft()
        if u not in explored:
            explored.append(u)
        for n in G[u]:
            if n in explored:
                continue
            else:
                queue.append(n)
    return explored

result = bfs(g1,'A')
print(result)
def dfs(G,s):
    explored = []
    queue = list([s])
    while queue:
        u = queue.pop()
        if u not in explored:
            explored.append(u)
        for n in G[u]:
            if n in explored:
                continue
            else:
                queue.append(n)
    return explored
result = dfs(g1,'A')
print(result)
def spf(G,s,d):
    explored = set()
    heap = [(0,s)]
    while heap:
        # print(heap)
        c,u = heapq.heappop(heap)
        # print(c,u)
        if u in explored:
            continue
        else:
            explored.add(u)
            # print(explored)
        if u==d:
            return c
        # print(G[u])
        for v,cost in G[u]:
            # print(v,cost)
            if v in explored:
                continue
            else:
                new = c+cost
                heapq.heappush(heap,(new,v))
    return -1
print(spf(g2,'E','F'))
# print(g2['E'])

