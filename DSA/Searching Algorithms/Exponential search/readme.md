# Exponential search
In computer science, an exponential search (also called doubling search or galloping search or Struzik search) is an algorithm, created by Jon Bentley and Andrew Chi-Chih Yao in 1976, for searching sorted, unbounded/infinite lists. There are numerous ways to implement this with the most common being to determine a range that the search key resides in and performing a binary search within that range. This takes O(log i) where i is the position of the search key in the list, if the search key is in the list, or the position where the search key should be, if the search key is not in the list.

Exponential search can also be used to search in bounded lists. Exponential search can even out-perform more traditional searches for bounded lists, such as binary search, when the element being searched for is near the beginning of the array. This is because exponential search will run in O(log i) time, where i is the index of the element being searched for in the list, whereas binary search would run in O(log n) time, where n is the number of elements in the list.

## Algorithm
Exponential search allows for searching through a sorted, unbounded list for a specified input value (the search "key"). The algorithm consists of two stages. The first stage determines a range in which the search key would reside if it were in the list. In the second stage, a binary search is performed on this range. In the first stage, assuming that the list is sorted in ascending order, the algorithm looks for the first exponent, j, where the value 2^j is greater than the search key. This value, 2^j becomes the upper bound for the binary search with the previous power of 2, 2^(j - 1), being the lower bound for the binary search.

In each step, the algorithm compares the search key value with the key value at the current search index. If the element at the current index is smaller than the search key, the algorithm repeats, skipping to the next search index by doubling it, calculating the next power of 2. If the element at the current index is larger than the search key, the algorithm now knows that the search key, if it is contained in the list at all, is located in the interval formed by the previous search index, 2^(j - 1), and the current search index, 2^j. The binary search is then performed with the result of either a failure, if the search key is not in the list, or the position of the search key in the list.

## Performance
       Case	        |      Runtime
    ----------------------------------
    Best	        |        O(1)
    Average	        |        O(log i)
    Worst	        |        O(log i)
    Auxiliary Space |	 O(1)

    Here i is the index of the key.