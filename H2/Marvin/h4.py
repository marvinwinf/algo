def rotate_list(l, s):
    '''
    Function to rotate a list depending on the given rotator argument. 
    s < 0: left rotation
    s > 0: right rotation 
    '''

    # Reduce steps for large numbers
    s = s % len(l)

    if s > 0:
        for i in range(s):
            shift_right(l)

    if s < 0:
        rotator = abs(s)
        for i in range(rotator):
           shift_left(l)


# Definition for right rotation
def shift_right(l):
    print("step")
    for i in range(len(l)-1):
        swap(l, 0, i+1)

# Definition for right rotation
def shift_left(l):
    for i in range(len(l)-1):
        swap(l, len(l)-1, len(l)-2-i)

def swap(l, i, j):
    value = l[i]
    l[i] = l[j]
    l[j] = value
