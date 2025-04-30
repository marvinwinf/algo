from graph import Graph

def swap(l, i, j):
    h = l[i]
    l[i] = l[j]
    l[j] = h

def update(todo_list, new_dist, entry, curr_path):
    # compute index of entry in todo list or where it will be added
    i = 0
    while i < len(todo_list) and todo_list[i][1] != entry:
        i = i + 1

    # append or update entry
    if i == len(todo_list):
        # Added extra entry to the current path list of each node
        todo_list.append((new_dist, entry, curr_path + [entry]))
    elif todo_list[i][0] > new_dist:
        # Removed the last entry because we could reach the node with our recent newest one
        todo_list[i] = (new_dist, entry, curr_path[-1:] + [entry])
    

    # move entry to the left so the todo list stays sorted
    while i > 0 and todo_list[i - 1][0] > todo_list[i][0]:
        swap(todo_list, i - 1, i)
        i = i - 1

def dijkstra(graph, start, dest):
    visited = []
    # Added a path list for our todo list
    todo = [(0, start, [start])]

    while len(todo) > 0 and todo[0][1] != dest:
        dist, node, path = todo[0]
        todo = todo[1:]  # remove first entry of todo list
        visited.append(node)
        for label, succ in graph.get_succs(node):
            if not succ in visited:
                # Added the current path for the updating function
                update(todo, dist + float(label), succ, path)

    if len(todo) == 0:
        return None
    else:
        # Adjusted return and added path
        return (todo[0][0],todo[0][2])  # return distance of destination node

'''
The following code can be used to work with Kiel City map.
The user can either enter the street name (node label) or a node ID
from the file 'kiel_city.csv'.

You can try: Olshausenstraße and Ringstraße
or 10905268916 and 821857536

You can also try: Kaistraße and Olshausenstraße
or 308421842 and 10905268916

However, this implementation of Dijkstra's algorithm is still a
prototype and not very fast. It will be improved later in the lecture.
'''

def input_node(g, prompt):
    '''
    Show prompt and read start and destination node from user.
    Nodes can be given as street name (= node label) or node ID.
    '''
    node = input(prompt)
    if g.has_node(node):
        # user has entered an existing node ID
        return node
    node_with_label = g.get_nodes_by_label(node)
    if node_with_label != []:
        # user has entered an existing node label,
        # return ID of first node with this label
        return node_with_label[0]
    else:
        print('Kein Knoten mit dieser ID oder diesem Label!')
        return None


g = Graph.from_file('kiel_city.csv')

start = input_node(g, 'Start: ')
dest = input_node(g, 'Ziel:  ')
result = dijkstra(g, start, dest)

if result is None:
    print("No result")

else: 
    distance, route = dijkstra(g, start, dest)

    # Combine url    
    url = "https://www-ps.informatik.uni-kiel.de/~fhu/CGI/route/path.cgi?path="
    for node in route:
        url= url+node + ","
    print(distance)
    
    # Remove last comma, but does work anyway
    print(url[:-1])
