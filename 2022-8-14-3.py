# num_nodes,num_edges = list(map(int,input('please input  nodes and edges').strip().split()))
# print(num_nodes,num_edges)
# edges = []

# for i in range(num_edges):
    # node1,node2,cost = list(map(int,input('').strip().split()))
    # print(node1,node2,cost)
    # edges.append((i,node1,node2,cost))
num_nodes=4
num_edges=5
edges = [
        (0,0,1,2),
        (1,0,2,3),
        (2,0,3,4),
        (3,1,2,3),
        (4,2,3,2)
        ]
edges = sorted(edges,key=lambda edge:edge[3])
parent = list(range(num_nodes))
print(parent)

def find_parent(i):
    if i != parent[i]:
        print(i,'parent[i]:',parent[i])
        parent[i]=find_parent(parent[i])
    return parent[i]

min_spanning_tree_cost=0
min_spanning_tree = []

for edge in edges:
    
    print('edge:',edge)
    parent_a = find_parent(edge[1])
    parent_b = find_parent(edge[2])
    print('parent_a:',parent_a)
    print('parent_b:',parent_b)
    print('\n')
    if parent_a != parent_b:
        min_spanning_tree_cost+=edge[3]
        min_spanning_tree.append(edge)
        parent[parent_a]=parent_b

print(min_spanning_tree_cost)
for edge in min_spanning_tree:
    print(edge)
