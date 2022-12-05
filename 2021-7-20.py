#import  gen_num
import heapq
from  weighted_G import G,printG
printG()
# print(G)

def spf(G,s,d):
    visited = []
    queue = [(0,s)]
    while queue:
        c,u = heapq.heappop(queue)
        if u in visited:
            continue
        else:
            

