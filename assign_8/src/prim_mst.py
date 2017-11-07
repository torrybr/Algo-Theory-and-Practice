import heapq
import random


########################## Start helper files #############################################

def name(i):
    return 'v' + hex(i)[2:]


def generate_weighted_undirected_graph_edges(vertex_count, seed=0):
    """Describe a weighted, undirected, connected graph by returning
    a list of its edges in the form of (node1, node2, weight). The edge list
    returned is a pure function of the inputs, and is therefore reproducible.
    You could email your friend the vertex count and seed you used, and they
    could produce the same graph you have! This could make it easier to
    compare performance."""
    r = random.Random()
    r.seed(seed)

    # Ensure the graph is connected (or else we won't be able to find an MST)
    # The vertices are represented by the numbers [0, vertex_count).
    # Start by giving each vertex an edge to a lower-numbered vertex,
    # making a tree.
    E = set()
    for i in range(1, vertex_count):
        edge = (r.choice(range(i)), i)
        E.add(edge)

    # Decide how many edges the graph will have.
    edge_count = int(vertex_count * r.choice([1.5, 3, 5, 10, vertex_count / 4]))
    edge_count = min(edge_count, int(vertex_count * vertex_count / 4))

    # Populate the graph with extra edges.
    while len(E) < edge_count:
        # Randomly select pairs of vertices.
        edge = r.sample(range(vertex_count), k=2)
        # Using a set and describing edges in sorted vertex order.
        # This ensures we won't have duplicate edge records.
        E.add(tuple(sorted(edge)))

    # Create a set of weights for the edges.
    # With no duplicates edge weights, the MST of the resulting graph is unique.
    weights = list(range(edge_count))
    r.shuffle(weights)

    return [(name(v1), name(v2), w) for (v1, v2), w in zip(sorted(E), weights)]


def write_graph_edges_to_file(filename, edges):
    with open(filename, mode='w') as f:
        for v1, v2, w in edges:
            f.write("{} {} {}\n".format(v1, v2, w))


#################################### I can never get the files to import ###############################################

def write_tree_edges_to_file(edges, filename):
    # TODO write out the edges, one per line. The same format as produced by generate_mst_input
    pass


# Do not change this function's name or the arguments it takes. Also, do not change
# that it writes out the results at the end.
# This is the full contract of you code (this function in this file). Otherwise,
# please feel free to create helpers, modify provided code, create new helper files, etc.
# Whatever you turn in is what we will grade (ie we won't provide any files or overwrite
# any of yours)
# Have fun!
def compute_mst(filename):
    '''Use Prim's algorithm to compute the minimum spanning tree of the weighted undirected graph
    described by the contents of the file named filename.'''
    tree_edges = []
    # TODO compute the edges of a minimum spanning tree
    write_tree_edges_to_file(tree_edges, filename + '.mst')


if __name__ == '__main__':
    # generate graph
    generate_mst_input()
