def Sum_array_sum_k(n,arr,k):
    prefix_sum = 0

    count = 0

    prefix_dict = {0:1,}

    for num in arr:
        prefix_sum += num
        
        if (prefix_sum - k) in prefix_dict:
            count += prefix_dict[prefix_sum-k]

        if prefix_sum in prefix_dict:
            prefix_dict[prefix_sum] += 1
        else:
            prefix_dict[prefix_sum] = 1
    
    return count


T = int(input())
while (T >0):
    n = int(input())
    arr = list(map(int,input().split()))
    k = int(input())
    print(Sum_array_sum_k(n,arr,k))
    T-= 1
