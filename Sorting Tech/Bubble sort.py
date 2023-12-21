def Bubble_sort(given_list):
    for i in range(len(given_list)):
        for j in range(len(given_list)-1):
            if given_list[j+1] < given_list[j]:
                given_list[j],given_list[j+1] = given_list[j+1],given_list[j]
    return given_list
print(Bubble_sort([67,5,69,7,70]))