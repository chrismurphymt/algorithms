import numpy
n=8
def draw(g, unweighted_mst_edges):
    import pylab as P
    pos = networkx.circular_layout(g)
    networkx.draw_networkx(g, pos=pos, with_labels=True, node_color='white')
    #print unweighted_mst_edges
    t_star = networkx.from_edgelist(unweighted_mst_edges)
    #print t_star.edges()
    networkx.draw_networkx_edges(t_star, pos=pos, node_color='white',width=3)
    edge_labels=dict([ (e,A[e[0],e[1]]) for e in g.edges() ])
    networkx.draw_networkx_edge_labels(g, pos=pos, edge_labels=edge_labels)
    P.show()
numpy.random.seed(0)# create an adjacency matrix:
A = numpy.random.randint(0,100,(n,n))
for i in range(n):
    # make distance from i to i 0:
    A[i,i] = 0
    for j in range(i+1,n):
        # make distance from i to j match the distance from j to i# (i.e., make into an undirected graph):
        A[i,j] = A[j,i]
mst_edges = []
# start with node 0 in the MST
nodes_used = set([0])
nodes_not_used = set([ i for i in range(n) ])
# in each iteration, grow the include nodes to the next node connected:
while len(nodes_used) != n:
    edges_between_included_and_not_included = []
    # runtime: |nodes_used| * (n-|nodes_used|)
    for i in nodes_used:
        for j in nodes_not_used:
            edges_between_included_and_not_included.append( (A[i,j], i, j) )

    # add minimum weight edge between included and not included nodes:
    best_edge = min(edges_between_included_and_not_included)
    mst_edges.append(best_edge)
    # best edge is of form (weight, i, j) where j is a node not used:
    node_not_yet_used = best_edge[2]
    # runtime from the following lines will each be \in \Theta(n# \log(n)) using balanced binary tree sets:
    nodes_used.add(node_not_yet_used)
    nodes_not_used.remove(node_not_yet_used)
print ('MST cost', sum( [ e[0] for e in mst_edges ] ))
print (mst_edges)
import networkx
g = networkx.from_numpy_matrix(A)
draw(g, [ (e[1],e[2]) for e in mst_edges ] )


#Metric: cost( A->B->C) >= cost(A->C)
