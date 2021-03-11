# Jump search
With Jump Search, the sorted array of data is split into subsets of elements called blocks. We find the search key (input value) by comparing the search candidate in each block. As the array is sorted, the search candidate is the highest value of a block.

## Algorithm
With Jump Search, the sorted array of data is split into subsets of elements called blocks. We find the search key (input value) by comparing the search candidate in each block. As the array is sorted, the search candidate is the highest value of a block.

When comparing the search key to a search candidate, the algorithm can then do 1 of 3 things:

If the search candidate is lesser than the search key, we'll check the subsequent block
If the search candidate is greater than the search key, we'll do a linear search on the current block
If the search candidate is the same as the search key, return the candidate
The size of the block is chosen as the square root of the array's length. Therefore, arrays with length n have a block size of √n, as this on average gives the best performance for most arrays.

It might be useful to illustrate how it works. Here's how Jump Search would fine the value 78 in an array of 9 elements:

<p align="center">
  <img src="https://stackabuse.s3.amazonaws.com/media/jump-search-in-python-1.jpg">
</p>

## Performance
The optimal size of a block to be jumped is (√ n). This makes the time complexity of Jump Search O(√ n). The time complexity of Jump Search is between Linear Search ((O(n)) and Binary Search (O(Log n).