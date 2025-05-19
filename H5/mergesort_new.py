import random
import sys

def mergesort(inlist):
    length = len(inlist)
    outlist = [] # Ausgabeliste erstellen in der Länge von inlist
    for i in range(len(inlist)):
        outlist.append(0)
    
    def merge(l1, l2, start_left, start_right, end):
        l = start_left  
        r = start_right
        out = start_left
        
        while l < start_right and r < end:
            if l1[l] <= l1[r]:
                l2[out] = l1[l]
                l = l + 1
            else:
                l2[out] = l1[r]
                r = r + 1
            out = out + 1
        
        while l < start_right:
            l2[out] = l1[l]
            l = l + 1
            out = out + 1

        while r < end:
            l2[out] = l1[r]
            r = r + 1
            out = out + 1       
    # neue Variante des merge-Teil innerhlab von mergesort endet
    
    l1 = inlist
    l2 = outlist
    
    to_merge = 1
    
    while to_merge < length:
        sort = 2 * to_merge
        
        for left_start in range(0, length, sort):
            right_start = left_start + to_merge
            end = left_start + sort

            if right_start >= length:
                break
        
            if end > length:
                end = length
        
            merge(l1, l2, left_start, right_start, end)
        
        l1, l2 = l2, l1 # tausch der Listen
        to_merge = to_merge * 2 # zu mischende Teillisten vergrößern
    return l1

#Tests

def large_rand_list(n): # Funktion zum generieren von Listen
    res = []
    for i in range(n):
        res.append(random.randint(1,n * 2))
    return res

l = large_rand_list(10)
print(l)
l = mergesort(l)
print(l)