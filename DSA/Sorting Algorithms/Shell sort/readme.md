# Shell sort
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. This algorithm avoids large shifts as in case of insertion sort, if the smaller value is to the far right and has to be moved to the far left.

This algorithm uses insertion sort on a widely spread elements, first to sort them and then sorts the less widely spaced elements. This spacing is termed as interval. This interval is calculated based on Knuth's formula as −

Knuth's Formula

    h = h * 3 + 1
    where − 
        h is interval with initial value 1

## Algorithm
The idea is to arrange the list of elements so that, starting anywhere, taking every hth element produces a sorted list. Such a list is said to be h-sorted. It can also be thought of as h interleaved lists, each individually sorted. Beginning with large values of h allows elements to move long distances in the original list, reducing large amounts of disorder quickly, and leaving less work for smaller h-sort steps to do. If the list is then k-sorted for some smaller integer k, then the list remains h-sorted. Following this idea for a decreasing sequence of h values ending in 1 is guaranteed to leave a sorted list in the end.

In simplistic terms, this means if we have an array of 1024 numbers, our first gap (h) could be 512. We then run through the list comparing each element in the first half to the element in the second half. Our second gap (k) is 256, which breaks the array into four sections (starting at 0,256,512,768), and we make sure the first items in each section are sorted relative to each other, then the second item in each section, and so on. In practice the gap sequence could be anything, but the last gap is always 1 to finish the sort (effectively finishing with an ordinary insertion sort).

## Performance
#### The best case ∊ O(nlogn):
The best-case is when the array is already sorted. The would mean that the inner if statement will never be true, making the inner while loop a constant time operation. Using the bounds you've used for the other loops gives O(nlogn). The best case of O(n) is reached by using a constant number of increments.

#### The worst case ∊ O(n^2):
Given your upper bound for each loop you get O((log n)n^2) for the worst-case. But add another variable for the gap size g. The number of compare/exchanges needed in the inner while is now <= n/g. The number of compare/exchanges of the middle while is <= n^2/g. Add the upper-bound of the number of compare/exchanges for each gap together: n^2 + n^2/2 + n^2/4 + ... <= 2n^2 ∊ O(n^2). This matches the known worst-case complexity for the gaps you've used.

#### The worst case ∊ Ω(n^2):
Consider the array where all the even positioned elements are greater than the median. The odd and even elements are not compared until we reach the last increment of 1. The number of compare/exchanges needed for the last iteration is Ω(n^2).