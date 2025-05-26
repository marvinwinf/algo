import random
from myqueue import Queue

def merge(l1, l2): # helper function to merge two sorted lists l1, l2
    res = []
    i = 0
    j = 0
    
    # append smaller element and proceed in that list
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i = i + 1
        else:
            res.append(l2[j])
            j = j + 1
            
    # append remaining elements
    if i < len(l1):
        res.extend(l1[i:])
    else:
        res.extend(l2[j:])
    return res

# iterative mergesort with queue (non-mutating, returns new list)
def mergesort(l):
    # Create empty queue
    queue = Queue()

    for i in range(len(l)):
        queue.enqueue([l[i]]) # add a list containing the element to the queue

    while queue.head.next != queue.end: # repeat until only one list remains
    # Take the first two lists from the queue
        list1 = queue.dequeue()
        list2 = queue.dequeue()
        
        new_entry = merge(list1, list2)
        queue.enqueue(new_entry) # put result back into queue
    
    reslist = queue.dequeue()
    
    return reslist #Return resulting list

def randlist(n, a, b): # generate a list of length n with random elements between a and b
    res = []
    for i in range(n):
        res.append(random.randint(a, b))
    return res

# Test examples
l = [7, 2, 4, 3, 9]
l_new = mergesort(l) # eig. l
print(l_new)

# n = 10
# l = randlist(n, 1, 99)
# l = mergesort(l)
