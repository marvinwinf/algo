def list_fun(l):
    if len(l) < 2:
        return l
    else:
        return [l[0] + l[1]] + list_fun(l[2:])


l = [1,5,7,2,4,6,9]
print(list_fun(l))
print(list_fun([]))
print(l)