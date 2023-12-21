def partition(array,start,end):
    potential_index_for_pivot = start
    pivot = array[end]
    for j in range(start,end-1):
        if array[j] <= pivot :
            array[potential_index_for_pivot],array[j] = array[j],array[potential_index_for_pivot]
            potential_index_for_pivot += 1
    array[potential_index_for_pivot],array[end] = array[end],array[potential_index_for_pivot]
    # print(array)
    return potential_index_for_pivot

def Quick_sort(given_list,start,end):
    partition_index = partition(given_list,0,len(given_list)-1)
    Quick_sort(given_list,0,partition_index)
    Quick_sort(given_list,partition_index,end)


given_list = [12,9,7,15,10]
Quick_sort(given_list,0,len(given_list)-1)
print(given_list)