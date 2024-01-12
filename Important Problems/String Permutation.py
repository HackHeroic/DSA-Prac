def lettercasePermutation(str,i):
    if i == len(str):
        print(str)
        return
    s_lower = str[:i] + str[i].lower() + str[i+1:]
    lettercasePermutation(s_lower,i+1)
    s_upper = str[:i] + str[i].upper() + str[i + 1:]
    lettercasePermutation(s_upper, i + 1)

str = "abc"
i = 0
lettercasePermutation(str,i)