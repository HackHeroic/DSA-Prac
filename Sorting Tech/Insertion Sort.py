#One of the methods for doing insertion sort

def Isertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        storage = arr[i]
        j = i-1
        while j >= 0 and storage < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = storage
            j -= 1

    return arr

arr = [6,5,3,4]
print(Isertion_sort(arr))

