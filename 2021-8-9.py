from G import G 
print(G)
def dpf(G,s):
    queue = list([s])
    visited =set()
    while queue:
        u = queue.pop()
        if u in visited:
            continue
        else:
            visited.add(u)
        for v in G[u]:
            if v in visited:
                continue
            else:
                queue.append(v)
    return visited


print(dpf(G,'A')) 
