import random

def qsort_dance(l, start, end): # helper function to sort list l from index start to end (not included)
    if end - start > 1:
        pivot = l[start]
        m = start
        #print('->',start,end,m,l)
        for i in range(start + 1, end):
            if l[i] < pivot:
                m = m + 1
                l[m], l[i] = l[i], l[m]  # equals swap(l, m, i)
        l[start], l[m] = l[m], l[start]
        #print('<-',start, end,m,l)
        #input()
        qsort_dance(l, start, m)
        qsort_dance(l, m + 1, end)

def quicksort(l):
    qsort_dance(l, 0, len(l))

def randlist(n, a, b):
    res = []
    for i in range(n):
        res.append(random.randint(a, b))
    return res

# Test examples
l = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print(l)
quicksort(l)
print(l)

'''
l = [7, 2, 4, 3, 9, 8, 1, 5, 6]
print(l)
quicksort(l)
print(l)

'''
'''
n = 800000
l = randlist(n, 0, 2*n)
quicksort(l)
'''
