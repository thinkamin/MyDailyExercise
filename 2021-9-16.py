from G import G,weight_G
from collections import deque
import heapq
def bfs(G,s):
    queue = deque([s])
    visited = set()
    while queue:
        u =queue.popleft()
        # print(u)
        if u not in visited:
            visited.add(u)
        for v in G[u]:
            if v not in visited:
                queue.append(v)
    return visited
# print(bfs(G,'A'))
def dfs(G,s):
    queue = list([s])
    visited=set()
    while queue:
        u=queue.pop()
        if u not in visited:
            visited.add(u)
        for v in G[u]:
            if v not in visited:
                queue.append(v)
    return visited
# print(dfs(G,'A'))
def spf(G,s,d):
    heap = [(0,s)]
    visited=set()
    while heap:
        c,u = heapq.heappop(heap)
        print(c,u)
        if u in visited:
            continue
        else:
            visited.add(u)
        if u==d:
            return c
        for v,cost in G[u]:
            if v in visited:
                continue
            else:
                cost = cost+c
                heapq.heappush(heap,(cost,v))
    
    return -1
print(spf(weight_G,'A','E'))
