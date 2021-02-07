def bubbleSort(arr):
    n = len(arr) - 1

    for i in range(n):
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [11, 25, 12, 22, 64]

bubbleSort(arr)
print(arr)