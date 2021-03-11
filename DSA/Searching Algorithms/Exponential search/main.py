def binarySearch(arr, l, r, x):
    if r >= l: 
        mid = (int) (l + (r - l) // 2)
  
        if arr[mid] == x: return mid 
        elif arr[mid] > x: return binarySearch(arr, l, mid-1, x) 
        else: return binarySearch(arr, mid + 1, r, x) 
    else: 
        return -1

def exponentialSearch(arr, x):
    if arr[0] == x: return x

    length = len(arr)
    i = 1
    while i < length and arr[i] <= x:
        i *= 2

    return binarySearch(arr, i/2, min(i, length-1), x)

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
index = exponentialSearch(arr, 377)
print(index)