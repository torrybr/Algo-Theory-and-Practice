import copy
from collections import defaultdict
import sys


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

def read_weighted_undirected_graph(filename):
    """A helper to read the edges of a graph described in the file
    into a graph object."""
    g = Graph()
    with open(filename) as f:
        for line in f:
            try:
                v1, v2, w = line.split()
                g.add_edge(v1, v2, {'weight': int(w)})
            except:
                pass
    return g


def graph_files_equal(filename1, filename2):
    """Compares two graphs to see if they contain the same edges.
    Here, the files specifying the graphs describe one edge per line in
    the format: <a node> <another node> <weight of edge>, just like the
    format produced by the graph generator functions."""
    g1 = read_weighted_undirected_graph(filename1)
    g2 = read_weighted_undirected_graph(filename2)
    # Calls the __eq__(self, other) method of the g1 Graph object
    return g1 == g2


if __name__ == '__main__':
    # generate graph
    # write_graph_edges_to_file("small_input.txt", generate_weighted_undirected_graph_edges(5, 0))
    filename = sys.argv[1]
    filename2 = sys.argv[2]
    print(graph_files_equal(filename,filename2))
