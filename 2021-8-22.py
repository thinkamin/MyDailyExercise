from weighted_G import G,printG
import heapq
printG()
print(G)

def spf(G,s,d):
    heap = [(0,s)]
    visited = set()
    while heap:
        c,u = heapq.heappop(heap)
        # print(c,u)
        if u in visited:
            continue
        else:
            visited.add(u)
        if u == d:
            return c
        for v,cost in G[u]:
            if v in visited:
                continue
            cost = c+cost 
            print('2',cost,v)
            heapq.heappush(heap,(cost,v))
    return -1
print(spf(G,'E','F'))




