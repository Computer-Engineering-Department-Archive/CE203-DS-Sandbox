def selectionSort(arr):
    length = len(arr)
    for i in range (length):
        min = i
        for j in range (i+1, length):
            if arr[min] > arr[j]:
                min = j
        
        arr[i], arr[min] = arr[min], arr[i]

arr = [11, 25, 12, 22, 64]
selectionSort(arr)
print(arr)