from weighted_G import G,printG
import heapq
printG()

def spf(G,s,d):
    c,u = 0,s
    heap = [(0,s)]
    visited = set()
    while heap:
        cost,u = heapq.heappop(heap)
        if u in visited:
            continue
        else:
            visited.add(u)
        if u == d:
            return cost
        for v,c in G[u]:
            if v in visited:
                continue
            else:
                next = c + cost
                heapq.heappush(heap,(next,v))
    return -1
print(spf(G,'E','F'))




