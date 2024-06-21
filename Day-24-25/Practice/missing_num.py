def missing_num(array):
    array.sort()
    for i in range(len(array)):
        if array[i]!=i+1:
            return i+1
    return len(array)+1

array=[6, 1, 2, 8, 3, 4, 7, 10, 5]
print(missing_num(array))


