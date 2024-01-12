def func(arr,i,curr):
    if i == len(arr):
        print(set(curr))
        return
    a1 = curr[:] + [(arr[i])]
    func(arr,i+1,a1)
    func(arr,i+1,curr)

arr=[1,2,3]
func(arr,0,[])
