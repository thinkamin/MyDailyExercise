from weighted_G import G,printG
import heapq
# printG()

def bfs(G,s,d):
    visited = set()
    heap = [(0,s)]
    while heap:
        cost,u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == d:
            return cost
        for v,c in G[u]:
            next = c+cost
            heapq.heappush(heap,(next,v))
    return -1

print(bfs(G,'E','F'))


