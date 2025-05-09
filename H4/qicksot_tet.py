import random

def qsort_dance(l, start, end):
    if end - start <= 1:
        return
    
    i_c = start  # Zeiger für das zu vergleichende Element (mit Hut)
    i_h = end - 1  # Zeiger für das Hut-Element (Element am Ende)
    
    while i_c < i_h:
        if l[i_h] > l[i_c]:  # Wenn das Hut-Element größer ist als das zu vergleichende Element
            i_h -= 1  # Hut nach links weitergeben
        elif l[i_h] < l[i_c]:  # Wenn das Hut-Element kleiner ist als das zu vergleichende Element
            l[i_c], l[i_h] = l[i_h], l[i_c]  # Tauschen
            i_c += 1  # Zeiger für das zu vergleichende Element nach rechts verschieben
        else:
            i_h -= 1  # Hut weiter nach links verschieben, wenn die Elemente gleich sind
    
    qsort_dance(l, start, i_c)  # Rekursiv den linken Bereich sortieren
    qsort_dance(l, i_c + 1, end)  # Rekursiv den rechten Bereich sortieren

def quicksort(l):
    qsort_dance(l, 0, len(l))

def randlist(n, a, b):
    return [random.randint(a, b) for _ in range(n)]

# Testbeispiele
l = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print("Unsortierte Liste:", l)
quicksort(l)
print("Sortierte Liste:", l)
