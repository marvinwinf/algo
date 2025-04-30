def mergeSortedLists(l1, l2):
    i = 0 
    j = 0
    newlist = []
    
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            newlist = newlist + [l1[i]]
            i = i+1
        else:
            newlist = newlist + [l2[j]]
            j = j+1
            
    newlist = newlist + l1[i:]
    newlist = newlist + l2[j:]
            
    return newlist
            
s = [1, 4, 4, 5, 8, 9, 9]
t = [2, 5, 6]

merged = mergeSortedLists(s,t)
print(merged)
