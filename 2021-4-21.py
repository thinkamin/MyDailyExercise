from G import G,printG
printG()
def dfs(G,s):
    explored = set()
    queue = [s]

    while queue:
        v = queue.pop()
        if v in explored:
            continue
        explored.add(v)
        print(v)

        for w in G[v]:
            if w not in explored:
                queue.append(w)
    return explored
print(dfs(G,'A'))
