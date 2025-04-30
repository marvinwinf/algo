def check_sublist(l1, l2):

    if (len(l1) >= len(l2)):
        largerList = l1
        shorterList = l2
    else:
        largerList = l2
        shorterList = l1

    for l in range(len(largerList)):
        isValid = True
        for s in range(len(shorterList)):
            # Case: end of larger list
            if(l + s >= len(largerList)):
                isValid = False
            else: 
                # Case: Difference in s check run
                if(largerList[l+s] != shorterList[s]):
                    isValid = False
                else:
                    #Case: Found valid index
                    if (s == len(shorterList)-1 and isValid): 
                        return l

    # Case: No valid sublist given            
    return None

print(check_sublist([1, 2, 3, 4, 5], [3, 4]))
print(check_sublist([9, 7, 8], [9, 7, 8, 8, 9]))
print(check_sublist([1, 2, 3, 4, 5], [2, 4]))
print(check_sublist([4, 5, 4], [4, 5, 4]))
print(check_sublist([2], [1, 0, 1, 0, 0, 1, 0, 0, 1]))
print(check_sublist([1, 2, 3, 4, 5], [3, 4, 5]))
print(check_sublist([2, 1, 2, 1, 3, 2, 1, 3], [2, 1, 3, 1]))
print(check_sublist([4, 5, 4], [4, 5, 5]))