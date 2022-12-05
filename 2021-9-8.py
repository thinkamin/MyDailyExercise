from G import G,weight_G
print(G,weight_G)
from collections import deque
import heapq
def bfs(G,s):
    lst = deque([s])
    visited = set()
    while lst:
        u = lst.popleft()
        # print(u)
        if u not in visited:
            visited.add(u)
        for v in G[u]:
            if v not in visited:
                lst.append(v)
    return visited
# print(bfs(G,'A'))
def dfs(G,s):
    lst = list([s])
    visited = set()
    while lst:
        u = lst.pop()
        if u not in visited:
            visited.add(u)
        for v in G[u]:
            if v not in visited:
                lst.append(v)
    return visited
print(dfs(G,'A'))
def spf(G,s,d):
    heap = [(0,s)]
    visited = set()
    heapq.heapify(heap)
    while heap:
        c,u = heapq.heappop(heap)
        if u  in visited:
            continue
        else:
            visited.add(u)
        if u==d:
            return c
        for v,cost in G[u]:
            if v  in visited:
                continue
            else:
                c = cost+c
                heapq.heappush(heap,(c,v))
    return -1
print(spf(weight_G,'B','F'))

def gcm(a,b):
    c = a%b
    if c==0:
        return b
    if c==1:
        return -1
    else:
        return gcm(b,a%b)
print(gcm(16,4))




