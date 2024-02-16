def prefix_arr(arr):
    result = []
    result.append(arr[0])
    for i in range(1,len(arr)):
        result.append(result[i-1] + arr[i])

    return result

arr = list(map(int,input().split()))
k = int(input())

def Sum_till_k(arr,k):
    prefixed_arr = prefix_arr(arr)
    
