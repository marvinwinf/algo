import random
import time

def split_evenly(l):
    start = time.time()
    d_min = abs(sum(l))
    i_min = 0
    n = len(l)
    for i in range(1, n - 1):
        d = abs(sum(l[:i]) - sum(l[i:]))
        if d < d_min:
            d_min = d
            i_min = i

    end = time.time()
    print("Runtime (s): " + str(end - start))
    return d_min, i_min

def randlist(n, a, b):
    '''
    generate a list of length n with random elements between a and b
    '''
    res = []
    for i in range(n):
        res.append(random.randint(a, b))
    return res


# TODO: Measure runtime as described in the exercise

n = 1000
numbers = randlist(n, -100, 100)  # create random list of size n
result = split_evenly(numbers)
