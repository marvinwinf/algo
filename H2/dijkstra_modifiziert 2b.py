from graph import Graph

def swap(l, i, j):
    h = l[i]
    l[i] = l[j]
    l[j] = h

def update(todo_list, new_dist, entry):
    # compute index of entry in todo list or where it will be added
    i = 0
    while i < len(todo_list) and todo_list[i][1] != entry:
        i = i + 1

    # append or update entry
    if i == len(todo_list):
        todo_list.append((new_dist, entry))
    elif todo_list[i][0] > new_dist:
        print("old way: ", todo_list[i][0]) # vorherige Distanz
        todo_list[i] = (new_dist, entry)
        print("update: ", i, todo_list[i]) # gibt mir den Index innerhalb der To-Do Liste und die neue Distanz mit entsprechendem Knoten

    # move entry to the left so the todo list stays sorted
    while i > 0 and todo_list[i - 1][0] > todo_list[i][0]:
        swap(todo_list, i - 1, i)
        i = i - 1

def dijkstra(graph, start, dest):
    visited = []
    todo = [(0, start)]

    while len(todo) > 0 and todo[0][1] != dest:
        dist, node = todo[0]
        todo = todo[1:]  # remove first entry of todo list
        visited.append(node)
        for label, succ in graph.get_succs(node):
            if not succ in visited:
                update(todo, dist + float(label), succ)

    if len(todo) == 0:
        return None
    else:
        return todo[0][0]  # return distance of destination node


# Example with router network (nodes R1, ..., R5)

g = Graph.from_file('routers.csv')

print(g.get_nodes())

startnodes = ["R1", "R2", "R3", "R4", "R5"]
zielnodes = ["R1", "R2", "R3", "R4", "R5"]

for i in range(len(startnodes)):
    start = startnodes[i]
    for j in range(len(startnodes)):
        dest = zielnodes[j]
        if start == dest:
            break    
        else:
            print(start, dest) # zeigt an, welche Knoten gerade gewählt wurden
        result = dijkstra(g, start, dest)
        print("shortest distance:", result)
