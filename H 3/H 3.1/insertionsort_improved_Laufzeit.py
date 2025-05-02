import random

def swap(l, i, j):
    h = l[i] 
    l[i] = l[j]
    l[j] = h

def insertionsort(l): # function sorts the given list l by insertionsort
    for i in range(1, len(l)):
        j = i                              
        while j > 0 and l[j - 1] > l[j]:   
            swap(l, j - 1, j)
            j = j - 1   

def insertionsort_impr(l):
    sorted = 1 # zeigt an, bis zu welchem Index die Liste sortiert ist
    
    while sorted < len(l):
        x = l[sorted]      # speichert das letzte Element des sortierten Bereichs
        
        if l[sorted-1] < l[sorted]:
            sorted = sorted + 1
        else:
            i = sorted -1 
            while i >= 0 and l[i] > x:
                    l[i+1] = l[i]
                    i = i - 1
            l[i+1] = x
            sorted = sorted + 1

def shuffled_list(n): # create randomly shuffled list containing numbers 1, ..., n

    # create list [1, ..., n] using list comprehension
    res = [i for i in range(1, n+1)]
    # shuffle list randomly
    random.shuffle(res)
    return res

# Test examples
n = 1000
numbers = shuffled_list(n)
n1 = [] + shuffled_list(n)
n2 = [] + shuffled_list(n)

import time

while n < 1000000000: 
    start_time = time.time()
    insertionsort(n1)
    end_time = time.time()

    time_measured = end_time - start_time
    print('Runtime:', time_measured, 'sec')

    start_t = time.time()
    insertionsort_impr(n2)
    end_t = time.time()

    time_m = end_t - start_t
    print('Runtime:', time_m, 'sec')

    c = time_measured - time_m # zeigt die Differenz in der Laufzeit
    print(c)
    
    n = 10 * n