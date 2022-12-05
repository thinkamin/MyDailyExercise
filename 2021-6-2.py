from  weighted_G import G,printG
import heapq
printG()
print(G)
def spf(G,s,d):
    heap = [(0,s)]
    visited = set()
    while heap:
        cost,u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == d:
            return cost
        for v,c in G[u]:
            if v in visited:
                continue
            else:
                next = cost+c
                heapq.heappush(heap,(next,v))
    return -1

print(spf(G,"E","F"))
