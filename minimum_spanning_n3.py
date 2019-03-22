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

import heapq

mst_edges = []
# start with node 0 in the MST
nodes_used = set([0])
nodes_not_used = set([ i for i in range(n) ])
# in each iteration, grow the include nodes to the next node connected:

cut_edges = []
for j in range(1,n):
    heapq.heappush(cut_edges, (A[0,j], 0 , j))

while len(nodes_used) != n:
    best_edge = heapq.heappop(cut_edges)

    mst_edges.append(best_edge)

    node_not_yet_used = best_edge[2]

    nodes_used.add(node_not_yet_used)
    nodes_not_used.remove(node_not_yet_used)

    new_cut_edges = []
    for edge in cut_edges:
        if edge[2] != node_not_yet_used:
            new_cut_edges.append(edge)
    cut_edges = new_cut_edges
    heapq.heapify(cut_edges)
    for i in nodes_not_used:
        heapq.heappush(cut_edges, (A[node_not_yet_used,i], node_not_yet_used,i))

print ('MST cost', sum( [ e[0] for e in mst_edges ] ))
print (mst_edges)

import networkx
g = networkx.from_numpy_matrix(A)
draw(g, [ (e[1],e[2]) for e in mst_edges ] )


#Metric: cost( A->B->C) >= cost(A->C)
