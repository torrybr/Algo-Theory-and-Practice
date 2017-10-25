import graph


def read_topo_sort_from_file(filename):
    """This reads the first line of the file. In a topological sort solution file,
    the first line holds the nodes in topological sort order on the first line,
    separated by whitespace."""
    with open(filename) as f:
        string = f.readline()
    return string


def parse_tps(tps_str):
    """ Gets a string of ordering of nodes for topological
    ordering and creates a list of integers from that. """
    return [int(x) for x in tps_str.split()]


def contains_sink_node(graph):
    """ Checks if there is a node without outgoing edge. """
    # empty collections are boolean false, so this asks if all
    # nodes have a non-empty set of neighbors (outgoing edges)
    return all(graph[i] for i in graph)


def check_TPS(graph, tps):
    """ Takes a out-edge graph dictionary and a list of integers for
    topological ordering and checks if that topological ordering is correct. """
    for i in reversed(range(len(tps))):
        for j in range(i):
            if tps[j] in graph[tps[i]]:
                print("Fault: There is a backward edge from ", tps[i], " to ", tps[j])
                return False
    if len(graph.keys()) != len(tps):
        return False
    return True


def write_tps_to_file(tps, filename):
    with open('output_' + filename, 'w') as file:
        for node in tps:
            file.write(node + ' ')


def compute_tps(filename):
    """ Write your implementation to create a topological sort here. 
    Store your answer in tps"""
    """ <filename> is the name of the input file containing graph information:
    you need to read it in and perform the topological sort, saving the results
    in tps, then use write_tps_to_file() to output it to a file called output_<filename>"""
    tps = []
    write_tps_to_file(tps, filename)


if __name__ == '__main__':
    """ Write code here to run compute_tps for your testing purposes"""
    import sys
    filename = sys.argv[1]
    compute_tps(filename)
