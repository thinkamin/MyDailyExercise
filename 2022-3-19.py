# from my import gen_num
# from collections import namedtuple
from my import G1,G2
from collections import deque
# num_lst = gen_num()
print('G1()',G1())
print('G2()',G2())

G1 = G1()

def bfs(G,start):
    queue = deque([start]) 
    result = set() 
    while queue:
        u = queue.popleft()
        if u not in result:
            result.add(u)
            # print(result)
        for i in G[u]:
            if i in result:
                continue
            else:
                queue.append(i)
    return result
print(bfs(G1,'A'))
def dfs(G,start):
    queue=deque([start])
    result=set()
    while queue:
        u = queue.pop()
        if u not in result:
            result.add(u)
            print(result)
        for i in G[u]:
            if i in result:
                continue
            else:
                queue.append(i)
    return result
print(dfs(G1,'A'))

#为什么会觉得 bellford算法和spf算法难？ 这里面到底难在哪里？


    
    

