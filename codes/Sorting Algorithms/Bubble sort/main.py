def bubbleSort(arr):
    n = len(arr) - 1

    for i in range(n):
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

# Driver code
arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))

bubbleSort(arr)
print(arr)