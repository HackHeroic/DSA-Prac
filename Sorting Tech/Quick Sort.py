# You need to return the sorted array
# arr: input array
# start: starting index of array
# end: end index of array


def partition(arr,start,end):
    pivot = arr[end]
    potential_index_for_pivot = start - 1

    for j in range(start,end):
        if arr[j] < pivot:
            potential_index_for_pivot += 1
            arr[potential_index_for_pivot],arr[j] = arr[j],arr[potential_index_for_pivot]
    
    arr[potential_index_for_pivot+1],arr[end] = arr[end],arr[potential_index_for_pivot+1]

    return potential_index_for_pivot + 1




def quick_sort(array, low, high):     
    if low < high:
        pivot = partition(array,low,high)
        quick_sort(array,low,pivot-1)
        quick_sort(array,pivot+1,high)

    return array

T = int(input())
while T> 0:
    T-= 1
    array = list(map(int,input().split()))
    low = 0
    high = len(array)-1
    print(quick_sort(array,low,high))

