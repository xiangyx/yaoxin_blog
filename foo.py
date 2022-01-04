def sum_even(array):
    res = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            print(array[i])
            res += array[i]
    return res
    

print(sum_even(list(range(0, 101, 2))))