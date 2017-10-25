def space_delimited_to_symbol_delimited(line):
    graph_viz_edge_symbol = '->'
    nodes = line.split()
    return ' '.join([nodes[0], graph_viz_edge_symbol, nodes[1]])

def base_name(file_name):
    return file_name.rpartition('.')[0].rpartition('/')[-1]

def file_to_graph_viz_representation(graph_file_name):
    with open(graph_file_name) as f:
        space_delimited_edges = f.readlines()
        symbol_delimited_edges = map(space_delimited_to_symbol_delimited,
                                     space_delimited_edges)
        return 'digraph {} {{\n{}\n}}'.format(base_name(graph_file_name),
                                              '\n'.join(symbol_delimited_edges))

def print_graph_viz_representation(graph_file_name):
    print(file_to_graph_viz_representation(graph_file_name))

def create_graph_viz_file_for(graph_file_name):
    '''Creates a graph viz format file from a space separated
    graph representation file. The name of the new file is the
    old file name with ".graph_viz" appended.'''
    with open(graph_file_name + '.graph_viz', 'w') as f:
        f.write(file_to_graph_viz_representation(graph_file_name))
        f.write('\n')
    return True
