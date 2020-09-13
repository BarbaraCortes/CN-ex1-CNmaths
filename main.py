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