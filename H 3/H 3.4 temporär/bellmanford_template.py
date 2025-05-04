from graph import Graph
from math import inf

'''
returns list of all edges as tuples (from, weight, to)
'''
def get_edges(graph):
    edges = []
    for node in graph.get_nodes():
        for label, succ in graph.get_succs(node):
            edges.append((node, float(label), succ))
    return edges

'''
computes length of shortest path from node start to node
dest in given graph using the Bellman-Ford algorithm
'''
def bellmanford(graph, start, dest):
    # Create dist dictionary with all nodes
    dist = {}
    edges = get_edges(graph)
    nodes = graph.get_nodes()

    for node in nodes:
        dist[node] = inf
    
    # Initilize nodes
    dist[start] = 0

    # TODO cancel loop
    i = 0
    is_different = True
    while i < len(nodes) and is_different: 
        for edge in edges:
            if dist[edge[2]] > dist[edge[0]] + edge[1]:
                dist[edge[2]] = dist[edge[0]] + edge[1]
                
                # Settings this to false to toggle in the end
                is_different = False
        i = i + 1 
        is_different = not(is_different)

    # Negative circles
    for edge in edges:
        if dist[edge[0]] != inf and dist[edge[2]] > dist[edge[0]] + edge[1]:
            return None

    if (dist[dest] != inf):
        return dist[dest]
    
    return None 


# Example with negative edge weights

#g = Graph.from_file('example_negative.csv')
#result = bellmanford(g, 'A', 'D')
#print(result)
