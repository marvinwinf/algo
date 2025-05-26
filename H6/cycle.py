def new_cycle(value): # constructs a cycle containing one element
    
    elem = {'value': value}
    elem['next'] = elem
    return elem # returns a pointer to this element

def get_node_value(node): #returns the value of the given node, constant runtime
    return node['value']

def add_next_node(node, value): # adds a node with the given value to the cycle
    # directly after the given node. returns a pointer to the new node, constant runtime

    old_next = node['next']
    new_elem = {'value': value, 'next' : old_next }
    node['next'] = new_elem
    return new_elem

def delete_next_node(node):
    # Test, ob es noch mehr als einen Knoten gibt
    if node['next'] == node: # wenn node nicht der einzige Knoten ist, kann gelöscht werden, sonst return False
        return False
    else:
        # Zeiger, der gelöscht werden soll
        x = node["next"]["next"]
        node["next"] = x
    return True
    
def delete_node(node):
    # Test, ob es noch mehr als einen Knoten gibt
    if node['next'] == node:
        return False # wenn node nicht der einzige Knoten ist, kann gelöscht werden, sonst return False
    else:
        # findet den Knoten, der vor node steht
        find_before = node
        while find_before["next"] != node:
            find_before = find_before["next"]
        find_before["next"] = node["next"] # der Vorgänger von node verweist auf den ehemaligen Nachfolger von node
        return True

def cycle_to_list(node): # return all values within the cycle as list, linear runtime in the number of elements in the cycle  
    pointer = node
    res = []
    while pointer['next'] != node:
        res.append(pointer['value'])
        pointer = pointer['next']
    res.append(pointer['value'])
    return res

# Testfälle für das Programm
e1 = new_cycle('A')
e2 = add_next_node(e1, 'B')
e3 = add_next_node(e1, 'C')
print(cycle_to_list(e1))

print(delete_node(e2))
print(cycle_to_list(e1)) 
print(delete_node(e1))
print(delete_node(e3))

e1 = new_cycle('A')
e2 = add_next_node(e1, 'B')
e3 = add_next_node(e1, 'C')
e4 = add_next_node(e1, 'D')     
e5 = add_next_node(e4, 'E')
print(cycle_to_list(e1))
print(delete_next_node(e4))
print(cycle_to_list(e1))