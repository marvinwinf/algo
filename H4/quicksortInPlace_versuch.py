import random

def qsort_dance(l, start, end): # helper function to sort list l from index start to end (not included)
    i_c = start # pointer für das zu vergleichende Element (pivot - Element)
    i_h = end-1 # pointer für das hut_Element
    
    if len(l) <= 1:
        return None
    
    else:
        compare_element = l[i_c]  # l[0] setzt einen Hut auf/ wird markiert
        hut_element = l[i_h]      # das Element an letzten Index setzt einen Hut auf
        
        print("compare_element:", compare_element) # Test
        print("hut_element:", hut_element)         # Test
        
        print("Poniter c:", i_c) # pointer auf das compare_element
        print("Pointer hut:", i_h) # pointer auf das hut_element
                    
        if l[i_h] > l[i_c]:
            i_h = i_h-1 # der Index des Hutelements verändert sich, da der Hut nach links weitergereicht wird
        
        if l[i_h] < l[i_c]: # Vergleich, ob das hut_element kleiner ist als das compare_element 
            c = i_c 
            h = i_h
            
            l[i_h], l[i_c] = l[i_c], l[i_h] # compare_element und hut_element tauschen
            print(l)
            i_c = h       # das compare_element steht an einer neuen Position, daher muss der Index aktualisiert werden
            i_h = c + 1 # das hut_elemet steht an einer neuen position
                        # der hut wird dann nach rechts weitergereicht und der pointer deshalb ebenfalls verschoben 
        
        if i_c == i_h: # das compare_element hat beide Hüte auf/ beide Pointer auf dem compare_element
            s_unsorted_left = 0
            e_unsorted_left = i_c-1
            
            sorted_area = [l[i_c]]
                if l[i_c] < sorted_area[0]:
                    l =
                    
            s_unsorted_right = i_c + 1
            e_unsorted_right = end
       
        #print(sorted_area)
        
        qsort_dance(l, s_unsorted_left, e_unsorted_left)
        qsort_dance(l, s_unsorted_right, e_unsorted_right = end)

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
