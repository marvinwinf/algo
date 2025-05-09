import random

def qsort_dance(l, start, end):
    
    if end - start <= 1:
        return None
    
    i_c = start  # Zeiger für das zu vergleichende Element/ Tänzer vorne mit Hut
    i_h = end - 1  # Zeiger für das Hut-Element/ Tänzer am letzten Index, ebenfalls mit Hut
    
    compare_element = l[start]  # das zu vergleichende Element ist zu Beginn immer das erste Element
    
    while i_c < i_h: # Solange das vergl. Element < ist als das Hut-Element
        while l[i_c] <= compare_element and i_c < i_h:
            i_c += 1 # den Pointer auf das zu vergleichende El. weiter nach rechts verschieben/ Hut weitergeben
            
        while l[i_h] >= compare_element and i_c < i_h: # solange das Hut-Element größer ist als das zu vergleichende Element
            i_h -= 1 # den Pointer auf das Hut-El. weiter nach links verschieben/ Hut weitergeben
        
        if i_c < i_h:
            l[i_c], l[i_h] = l[i_h], l[i_c]  # Tausche die Elemente
    
    l[start], l[i_h] = l[i_h], l[start] # das Hut-Element an die passende Stelle positionieren, an der der Tänzer steht, der aufhört zu tanzen
    
    qsort_dance(l, start, i_h) # Aufruf für die Seite links des bereits feststehenden Tänzers
    qsort_dance(l, i_h + 1, end) # Aufruf für die Seite rechts des bereits stehenden Tänzers

def quicksort(l):
    qsort_dance(l, 0, len(l))

def randlist(n, a, b):
    res = []
    for i in range(n):
        res.append(random.randint(a, b))
    return res

# Test
l = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print(l)
quicksort(l)
print(l)

l = [7, 2, 4, 3, 9, 8, 1, 5, 6]
print(l)
quicksort(l)
print(l)

n = 800000
l = randlist(n, 0, 2*n)
quicksort(l)