from weighted_G import G,printG
# printG()
import heapq
def shortestpath(G,s,d):
    cost = 0
    heap = [(cost,s)]
    visited = set()
    while heap:
        cost,u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if  u == d:
            return cost
        for v,c in G[u]:
            if v in visited:
                continue
            next = cost+c
            heapq.heappush(heap,(next,v))
    return -1 
print(shortestpath(G,'E',"F"))
