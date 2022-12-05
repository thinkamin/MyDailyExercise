from G import G,printG
printG()

def dfs(G,s):
    queue = list([s])
    visited = set()
    while queue:
        u = queue.pop()
        for v in G[u]:
            if v not in visited:
                queue.append(v)
        visited.add(u)
    return visited

print(dfs(G,'A'))
