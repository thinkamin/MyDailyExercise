from my  import G2
# print(G)
G=G2()
G_dct = []
for k,v in G.items():
    # print(k,v)
    for d,cost in v:
        G_dct.append((k,d,cost))
# print(G_dct)
nodes_num = len(G.keys())
edges_num = len(G_dct)
# print(nodes_num,edges_num)
edges = []
for i,(s,d,c) in enumerate(G_dct):
    edges.append((i,s,d,c))
print(edges)
edges = sorted(edges,key=lambda edge:edge[3])
parent = list(G.keys())
print(parent)

def find_parent(i):
    if i!= parent[i]:
        parent[i]=find_parent(parent[i])
    return parent[i]
mininum_spanning_tree_cost = 0
mininum_spanning_tree = []

for edge in edges:
    parent_a = find_parent(edge[1])
    parent_b = find_parent(edge[2])
    if parent_a!=parent_b:
        mininum_spanning_tree_cost+=edge[3]
        mininum_spanning_tree.append(edge)
        parent[parent_a] = parent_b
print(mininum_spanning_tree_cost)
for edge in mininum_spanning_tree:
    print(edge)

    
