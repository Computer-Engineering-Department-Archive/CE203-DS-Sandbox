import math

def jumpSearch(arr, x):
    length = len(arr)
    step = math.sqrt(length)
    prev = 0

    while arr[int(min(step, length)-1)] < x: 
        prev = step 
        step += math.sqrt(length) 
        if prev >= length: 
            return -1
       
    while arr[int(prev)] < x: 
        prev += 1
          
        if prev == min(step, length): return -1

    if arr[int(prev)] == x: 
        return prev 
      
    return -1

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
index = jumpSearch(arr, 377)
print(index)