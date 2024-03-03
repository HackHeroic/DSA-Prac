def merge_sorted_arrays(a,b):
    m = len(a)
    n = len(b)

    i = 0
    j = 0

    res = []

    while(i < m and j < n):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j+=1
        

    while(i < m):
        res.append(a[i])
        i += 1

    while(j < n):
        res.append(b[j])
        j += 1

    return res


a = [1,3,5,7]
b = [2,4,6,8]
print(merge_sorted_arrays(a,b))