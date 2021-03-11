def fibMonaccianSearch(arr, x):
    length = len(arr)
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1
 
    while (fibM < length):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
 
    offset = -1
 
    while (fibM > 1):
 
        i = min(offset+fibMMm2, length-1)
 
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
 
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
 
        else: return i
 
    if(fibMMm1 and arr[length-1] == x): return length-1
 
    return -1

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
index = fibMonaccianSearch(arr, 377)
print(index)