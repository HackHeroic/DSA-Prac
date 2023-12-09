
x = 1

def Binary_Search(n,arr,x):
    high = n-1
    low = 0
    high = n-1
    counter = 0
    while arr[0] >= x > arr[-1]:
        mid = low + (high - low)//2
        if arr[mid] == x:
            counter+=1
            arr.remove(1)  #can also use remove in this place
        elif arr[mid] < x:
            high = mid - 1
    return counter

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = Binary_Search(n,arr,x)
    print(ans)