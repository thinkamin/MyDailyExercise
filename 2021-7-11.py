from G import G,printG
printG()


def dfs(G,s):
    queue = list([s])
    visited = set()
    while queue:
        u = queue.pop()
        print(u)
        if u in visited:
            continue
        else:
            visited.add(u)
        for v in G[u]:
            if v not in visited:
                queue.append(v)
    return visited
print(dfs(G,'A'))
