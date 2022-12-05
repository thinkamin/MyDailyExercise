# from my import gen_num
# from collections import namedtuple
from my import G1,G2
from collections import deque
# num_lst = gen_num()

G1 = G1()

def bfs(G,s):
    finished = set()
    queue = deque([s])
    while queue:
        u = queue.popleft()
        if u not in finished:
            finished.add(u)
        print(u)
        for v in G[u]:
            if v in finished:
                continue
            else:
                queue.append(v)
        
        print('queue:',queue)
        print("finished:",finished)
    return finished

print(bfs(G1,'A'))


