import heapq
import random
import sys
import copy
from collections import defaultdict
import time


################################### undirected_graph.py #############################################################
def normalize_attributes(attributes):
    if attributes == None:
        attributes = {}
    if not isinstance(attributes, (dict, set)):
        raise ValueError('attributes must be a dict or a set')
    return attributes


class Graph:
    """An object to represent undirected graphs. Create one like:
    g = Graph()
    Then add nodes and edges to it like:
    g.add_edge("cat", "dog")
    g.add_node("mouse")
    You can associate arbitrary information with the nodes and edges like:
    g.add_edge("FC", "Denver", {"distance in miles": 53})
    Check out the other methods it defines.
    Feel free to modify it to your liking."""

    def __init__(self):
        self.nodes = {}
        self.edges = defaultdict(dict)

    def __repr__(self):
        return str({'nodes': self.nodes, 'edges': self.edges})

    def difference(self, other):
        """Try to report a specific difference between the two graphs,
        in a format that a human could understand to assist in debugging."""
        edge_set = set(self.get_edges())
        other_edge_set = set(other.get_edges())
        diff = edge_set ^ other_edge_set
        if diff:
            return diff
        for v, u in edge_set:
            if self.attributes_of(v, u) != other.attributes_of(v, u):
                return {(v, u): [self.attributes_of(v, u), other.attributes_of(v, u)]}
        return []

    def __eq__(self, other):
        return not bool(self.difference(other))

    def __ne__(self, other):
        return not (self == other)

    def copy(self):
        ret = Graph()
        ret.nodes = copy.deepcopy(self.nodes)
        ret.edges = copy.deepcopy(self.edges)
        return ret

    def add_node(self, identity, attributes=None):
        self.nodes[identity] = normalize_attributes(attributes)

    def ensure_node(self, identity):
        if identity not in self.nodes:
            self.add_node(identity)

    def add_edge(self, identity1, identity2, attributes=None):
        attributes = normalize_attributes(attributes)
        self.ensure_node(identity1)
        self.ensure_node(identity2)
        self.edges[identity1][identity2] = attributes
        self.edges[identity2][identity1] = attributes

    def get_nodes(self):
        return self.nodes.keys()

    def get_edges(self):
        return ((a, b) for a in self.edges for b in self.edges[a])

    def neighbors(self, identity):
        if identity in self.edges:
            return self.edges[identity].keys()
        return set()

    def attributes_of(self, identity, identity2=None):
        """Retrieve the attribute map (or set) associated with the arguments.
        Can be called with a single node, or with two nodes, which represents
        the edge between them."""
        if identity2 == None:
            return self.nodes[identity]
        return self.edges[identity][identity2]


########################## Start helper files #############################################

def read_lines(filename):
    with open(filename) as f:
        return f.readlines()


def parse_line(line):
    return [x for x in line.split()]


def read_by_row(filename):
    lines = read_lines(filename)
    return [parse_line(line) for line in lines]


def read_weighted_undirected_graph(filename):
    input_graph = Graph()
    with open(filename) as f:
        for line in f:
            try:
                v1, v2, w = line.split()
                input_graph.add_edge(v1, v2, {'weight': int(w)})
            except:
                pass
    return input_graph


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


def write_tree_edges_to_file(filename, edges):
    with open(filename, mode='w') as f:
        for v1, v2, w in edges:
            # print(v1,v2,w)
            f.write("{} {} {}\n".format(v1, v2, w))


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

    # The Priority Queue
    priorityq = []

    # The set of tuples that represent connected edges in the MST.
    connected = set()

    # Read the undirected weighted graph into a Graph() object.
    input_graph = read_weighted_undirected_graph(filename)

    # Choose a starting node Randomly from the "input_graph" nodes, set the current node to the random node chosen.
    current_node = random.choice(list(input_graph.get_nodes()))

    # The set of nodes that have been connected.
    tree = set()

    # Add the starting node to to the "tree" set so I know it is already in the Tree.
    tree.add(current_node)

    # For every neighbor of the "current_node" add that edge to the "priorityq"
    for v in input_graph.neighbors(current_node):
        heapq.heappush(priorityq, (input_graph.attributes_of(v, current_node)['weight'], current_node, v))

    '''The algorithm to traverse through tree using prims to find a Minimum Spanning Tree.
    This Runs until the (size of the connected set) is less than (the size of the total nodes in the input graph) - 1'''
    while len(connected) < len(input_graph.get_nodes()) - 1:

        # Pop the lowest weight of the "current_nodes" edges
        min_weight = heapq.heappop(priorityq)

        if min_weight[2] not in tree:
            tree.add(min_weight[2])
            best_edge = (min_weight[1], min_weight[2], min_weight[0])
            connected.add(best_edge)
            current_node = min_weight[2]
            for v in input_graph.neighbors(current_node):
                prev_edge = (v, current_node, input_graph.attributes_of(v, current_node)['weight'])
                prev_edge2 = (current_node, v, input_graph.attributes_of(v, current_node)['weight'])
                if prev_edge not in connected and prev_edge2 not in connected:
                    heapq.heappush(priorityq, (input_graph.attributes_of(v, current_node)['weight'], current_node, v))
    write_tree_edges_to_file(filename + '.mst', list(connected))


if __name__ == '__main__':
    #write_graph_edges_to_file("50000.txt", generate_weighted_undirected_graph_edges(50000, 0))
    filename = sys.argv[1]
    start_time = time.process_time()
    compute_mst(filename)
    end_time = time.process_time()
    print("Ran in: {:.5f} secs".format(end_time - start_time))

