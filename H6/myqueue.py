class ListElem():
    '''
    represents a linked list node
    '''
    def __init__(self):
        '''
        construct an empty list element
        '''
        self.empty = True

    def fill(self, value):
        '''
        fill list element with value and pointer
        to a new empty list element
        '''
        self.empty = False
        self.value = value
        self.next = ListElem()
        return self.next

class Queue():
    '''
    represents a queue consisting of linked nodes
    '''
    def __init__(self):
        '''
        constructs an empty queue
        '''
        empty_elem = ListElem()
        self.head = empty_elem
        self.end = empty_elem
        self.debug_output = True

    def enqueue(self, value):
        '''
        adds value to queue (FIFO order)
        '''
        self.end = self.end.fill(value)
        if self.debug_output:
            print('Queue: enqueue', value)

    def top(self):
        '''
        returns value of oldest element in the queue, without removing
        returns None if queue is empty
        '''
        if self.head.empty:
            return None
        else:
            return self.head.value

    def dequeue(self):
        '''
        removes oldest element from the queue and returns its value
        returns None if queue is empty
        '''
        if self.head.empty:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            if self.debug_output:
                print('Queue: deque', value)
            return value

    def is_empty(self):
        '''
        returns True if queue is empty, otherwise False
        '''
        return self.head.empty

    def __str__(self):
        '''
        return string representation of the queue (for debugging)
        '''
        res = []
        node = self.head
        while node is not self.end:
           res.append(node.value)
           node = node.next
        return str(res)
    
'''TestCode:
queue = Queue()
queue.enqueue([43])
queue.enqueue(73)
print(queue.top())
print(queue.dequeue())
'''