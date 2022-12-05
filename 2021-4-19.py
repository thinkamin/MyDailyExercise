from G import G,printG
printG()
def dfs(G,s):
    explored,stack = set(),[s]
    while stack:
        '''
    从屁股后面出，保证了深度优先
        '''
        v = stack.pop()

        if v in explored:
            continue
        explored.add(v)
        print(v)

        for w in G[v]:
            if w not in explored:
                stack.append(w)
                # print(w)
    return explored

print(dfs(G,'A'))
