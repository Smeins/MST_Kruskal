import networkx as nx
import matplotlib.pyplot as plt
T
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  
    parent = list(range(n))
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    mst = []
    for u, v, w in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            mst.append((u, v, w))
            parent[root_u] = root_v
        if len(mst) == n - 1:
            break
    return mst

edges = [(0, 1, 4), (0, 2, 4), (1, 2, 2), (1, 3, 6), (2, 3, 8), (3, 4, 9)]
n = 5
mst_edges = kruskal(n, edges)

G = nx.Graph()
G.add_weighted_edges_from(edges)

plt.figure(figsize=(10, 5))
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
edge_labels = {(u, v): w for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
plt.title("Originalgraph")
plt.show()

MST_G = nx.Graph()
MST_G.add_weighted_edges_from(mst_edges)

plt.figure(figsize=(10, 5))
nx.draw(MST_G, pos, with_labels=True, node_color='lightgreen', edge_color='red', node_size=2000, font_size=15)
mst_edge_labels = {(u, v): w for u, v, w in mst_edges}
nx.draw_networkx_edge_labels(MST_G, pos, edge_labels=mst_edge_labels, font_size=12)
plt.title("Minimum Spanning Tree (MST) mit Kruskal")
plt.show()
