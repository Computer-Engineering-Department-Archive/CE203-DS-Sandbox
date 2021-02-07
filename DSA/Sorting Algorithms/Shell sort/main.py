def shellSort(arr): 
    length = len(arr) 
    gap = length//3
  
    while gap > 0: 
  
        for i in range(gap,length): 
            temp = arr[i] 

            j = i 
            while  j >= gap and arr[j-gap] > temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            arr[j] = temp 
            
        gap //= 3

arr = [11, 25, 12, 22, 64]
shellSort(arr)
print(arr)