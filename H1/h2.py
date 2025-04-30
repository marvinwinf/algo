'''
Wir betrachten nach und nach jedes Element der Liste. Initial fügen wir bei einer nicht leeren Liste das erste Element zu einer Resultat Liste hinzu. 
Danach betrachten wir jedes weitere Element. Wenn sich der Wert zu unserem zuletzt hinzugefügten Element unterscheidet (andere Zahl), so können wir 
das Element hinzufügen. 
Ist das Element das gleich, so haben wir es bereiets hinzugefügt und wir brauchen es nichtmehr betrachten. 
'''
def removeDuplicates(l):
    result = []
    
    #Case list is empty
    if (len(l) == 0):
        return l

    result= [l[0]]

    for elem in l:
        if(result[len(result)-1] != elem):
            result = result + [elem]

    return result

