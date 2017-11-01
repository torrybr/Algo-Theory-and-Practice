from undirected_graph import Graph
import heapq


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
