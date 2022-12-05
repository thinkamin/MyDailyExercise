from weighted_G import G
import heapq
print(G)
def spf(G,s,d):
    visited = set()
    cost = 0
    heap = [(cost,s)]
    while heap:
        cost,u = heapq.heappop(heap)
        if u in visited:
            continue
        else:
            visited.add(u)
        if u==d:
            return cost
        for v,c in G[u]:
            if v in visited:
                continue
            else:
                next = c+cost
                heapq.heappush(heap,(next,v))
    return -1
print(spf(G,'B','F'))
print(spf(G,'B','C'))
