a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
def sel(a,b):
    c = []
    for d in a:
        if d in b:
            c.append(d)
    return c
i=set(sel(a,b))
print (list(i))






