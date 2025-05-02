import random

def selectionsort(l):
    '''
    sort given list by selectionsort algorithm
    the list is mutated
    '''
    for i in range(len(l) - 1):
        min_pos = i                          # find minimum starting
        for j in range(i + 1, len(l)):       #   at index i
            if l[j] < l[min_pos]:
                min_pos = j
        l[i], l[min_pos] = l[min_pos], l[i]  # swap l[i], l[min_pos]

def insertionsort(l):
    '''
    sorts given list by insertionsort algorithm
    the list is mutated
    '''
    for i in range(1, len(l)):
        j = i - 1
        while j >= 0 and l[j + 1] < l[j]:
            l[j], l[j + 1] = l[j + 1], l[j]  # swap l[j], l[j + 1]
            j = j - 1

def shuffled_list(n):
    '''
    create randomly shuffled list containing numbers 1, ..., n
    '''
    # create list [1, ..., n] using list comprehension
    res = [i for i in range(1, n+1)]
    # shuffle list randomly
    random.shuffle(res)
    return res

# Example
numbers = shuffled_list(10)
print(numbers)
selectionsort(numbers)
print(numbers)

'''
TODO: Measure runtime of sorting random lists of size
n = 1000, 2000, ..., 8000 and plot results
'''

import time

n = 1000
time_measured = 0

n_groesse = []
laufzeiten_selectionsort = []
laufzeiten_insertionsort = []

while n <= 8000:
    numbers = shuffled_list(n)

    start_time = time.time()
    selectionsort(numbers)
    end_time = time.time()

    time_measured = end_time - start_time
    print('Runtime for n =', n, ':', time_measured, 'sec')
    laufzeiten_selectionsort.append(time_measured)
    n_groesse.append(n)

    start_time = time.time()
    insertionsort(numbers)
    end_time = time.time()

    time_measured = end_time - start_time
    print('Runtime for n =', n, ':', time_measured, 'sec')
    laufzeiten_insertionsort.append(time_measured)

    n = n * 2  # verdoppelt n, bis man bei 8000 angekommen ist

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(n_groesse, laufzeiten_selectionsort)
ax.plot(n_groesse, laufzeiten_insertionsort)
plt.xlabel('n = Länge der Liste')
plt.ylabel('Zeit in Sekunden')
plt.title('Laufzeit in Abhängigkeit von der Größe der Liste')
plt.show()
