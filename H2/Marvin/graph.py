class Graph:
    '''
    Variant of the adjacency list implementation from the lecture
    in which arbitrary values (usually strings) can be used as
    node identifiers (key).
    Furthermore, each node can have an optional label.
    The implementation uses dictionaries (a hash map) to store
    adjacency lists and labels for node IDs.
    '''

    def __init__(self):
        '''
        the graph dictionary stores a pair consisting of node label
        and adjacency list for each node ID
        '''
        self.graph = {}

    def add_node(self, node, label=None):
        '''
        add node to the graph
        node is an identifier and label an otional node label
        if node does not exist, add it
        if label is given, update label for node ID
        '''
        if not node in self.graph:
            self.graph[node] = (label, [])
        elif label != None:
            adj_list = self.graph[node][1]
            self.graph[node] = (label, adj_list)

    def add_edge(self, start, label, dest):
        '''
        add edge with given edge label to graph
        if nodes (start and dest) do not exist, add nodes as well
        '''
        self.add_node(start)
        self.add_node(dest)
        self.graph[start][1].append((label, dest))

    def add_bi_edge(self, start, label, dest):
        '''
        add edge from start to dest an vice versa to graph
        if nodes (start and dest) do not exist, add nodes as well
        '''
        self.add_edge(start, label, dest)
        self.add_edge(dest, label, start)

    def has_node(self, node):
        '''
        check if node occurs in graph
        '''
        return node in self.graph

    def get_nodes(self):
        '''
        returns list of all node IDs
        '''
        return list(self.graph.keys())

    def get_succs(self, node):
        '''
        returns successors (with edge labels) from the given node
        produces a copy to avoid manipulation from outside
        '''
        return self.graph[node][1].copy()

    def get_node_label(self, node):
        '''
        returns node label of given node
        no copy needed, since usually strings (or other non-mutable types)
        are used
        '''
        return self.labels[node]

    def get_nodes_by_label(self, label):
        '''
        return all nodes with given label
        '''
        res = []
        for node in self.graph:
            if self.graph[node][0] == label:
                res.append(node)
        return res

    def __str__ (self):
        '''
        conversion to string
        '''
        return str(self.graph)

    @staticmethod
    def from_file(filename):
        '''
        static method to read graph from a CSV file
        '''
        file = open(filename, mode='r', encoding='utf8')
        lines = file.readlines()
        file.close()
        directed = lines[0].strip() == 'directed'
        graph = Graph()
        for line in lines[1:]:
            cols = line.strip().split(',')
            if len(cols) == 2: # node with label
                graph.add_node(cols[0], cols[1])
            else:
                if len(cols) == 4:
                    # edge with additional start node label
                    graph.add_node(cols[0], cols[3])
                if directed:
                    # add directed edge with edge label
                    graph.add_edge(cols[0], cols[1], cols[2])
                else:
                    # undirected graph is represented by directed
                    # graph with symmetric edges
                    graph.add_bi_edge(cols[0], cols[1], cols[2])

        return graph


# Example: Read graph from SH map file
if __name__ == "__main__":
    g = Graph.from_file('sh-map.csv')
    print(g)
    print("Nodes:", g.get_nodes())
    print("Number of nodes:", len(g.graph))
