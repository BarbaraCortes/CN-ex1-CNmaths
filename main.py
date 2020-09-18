import networkx as nx 

f = open('./wikispeedia_paths-and-graph/articles.tsv', 'r')
nodes = set()
for line in f:
	if line.startswith('#') or len(line.strip()) == 0:
		continue
	nodes.add(line.strip())

G = nx.DiGraph()

for nodeid in nodes:
	G.add_node(nodeid)

f = open('./wikispeedia_paths-and-graph/links.tsv', 'r')
for line in f:
	if line.startswith('#') or len(line.strip()) == 0:
		continue
	pair = line.strip().split()
	G.add_edge(pair[0], pair[1])

print('number of nodes:' + str(len(G.nodes)))
print('number of edges:' + str(len(G.edges)))

A = nx.adjacency_matrix(G.to_undirected())
A_3 = A.dot(A).dot(A)
A_4 = A_3.dot(A)
print('matrix X (A^3):' + str(A_3.count_nonzero()) + ' non zeros')
print('matrix Y (A^4):' + str(A_4.count_nonzero()) + ' non zeros')

A = nx.adjacency_matrix(G)
C = A.dot(A.transpose())
B = A.transpose().dot(A)
print('co-citation max value: ' + str(C.max()))
print('bibliographic coupling max value: ' + str(B.max()))

L_mutual = 0
for u in list(G.nodes()):
	for v in list(G.nodes()):
		if u != v and G.has_edge(u, v) and G.has_edge(v, u):
			L_mutual += 1;

print('reciprocity (traditional definition): ' + str(L_mutual/len(G.edges)))