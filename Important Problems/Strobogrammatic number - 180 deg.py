def isStrobo(n):
    length = len(str(n))
    my_fav_pairs = [[1, 1], [6, 9], [8, 8], [0, 0], [9, 6]]
    center_digits = [1, 0, 8]
    my_start_end = [int(str(n)[0]), int(str(n)[-1])]
    if my_start_end not in my_fav_pairs:
        return False
    else:
        Start = 0
        end = len(str(n)) - 1
        while Start < end:
            temp_list = [int(str(n)[Start]), int(str(n)[end])]
            if temp_list not in my_fav_pairs:
                return False
            Start += 1
            end -= 1
            if (Start == end) and (int(str(n)[Start]) not in center_digits):
                return False
            elif (Start == end) and (int(str(n)[Start]) in center_digits):
                return True
        return True


start, end = map(int, input().split())
count = 0


def Strobogrammatic_nos(start, end, count):
    if start > end:
        return count
    elif isStrobo(start):
        return Strobogrammatic_nos(start + 1, end, 1 + count)
    else:
        return Strobogrammatic_nos(start + 1, end, count)


print(Strobogrammatic_nos(start, end, count))
