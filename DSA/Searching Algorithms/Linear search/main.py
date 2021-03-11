def linearSearch(arr, x):
    length = len(arr)

    for i in range(length):
        if arr[i] == x:
            return i

    return -1

arr = [11, 25, 12, 22, 64]
index = linearSearch(arr, 12)
print(index)