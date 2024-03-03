def Binary_Search(n,arr,x):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid -1
        else:
            start += 1
    
    return -1

T = int(input())

while(T> 0):
    T -= 1
    n = int(input())
    arr = list(map(int,input().split()))
    x = int(input())
    ans = Binary_Search(n,arr,x)
    print(ans)


        
    

