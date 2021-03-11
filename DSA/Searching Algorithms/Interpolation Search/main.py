def interpolationSearch(arr, x):
    lo = 0
    hi = (len(arr) - 1)
 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x: return lo
            return -1
        
        pos  = lo + int(((float(hi - lo) / 
            (arr[hi] - arr[lo])) * (x - arr[lo])))

        if arr[pos] == x: return pos
        if arr[pos] < x: lo = pos + 1
        else: hi = pos - 1
    
    return -1

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
index = interpolationSearch(arr, 377)
print(index)