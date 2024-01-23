def func(arr,i,curr):
    if i == len(arr):
        return
    a1 = curr[:] + [(arr[i])]
    print(set(a1),end = " ")
    func(arr,i+1,a1)
    func(arr,i+1,curr)

arr=[1,2,3]
print(set([]),end = " ")
func(arr,0,[])
