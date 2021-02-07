In divide and conquer approach, the problem in hand, is divided into smaller sub-problems and then each problem is solved independently. When we keep on dividing the subproblems into even smaller sub-problems, we may eventually reach a stage where no more division is possible. Those "atomic" smallest possible sub-problem (fractions) are solved. The solution of all sub-problems is finally merged in order to obtain the solution of an original problem.

## Divide and Conquer
<p align="center">
  <img src="https://www.tutorialspoint.com/data_structures_algorithms/images/divide_and_conquer.jpg">
</p>
Broadly, we can understand divide-and-conquer approach in a three-step process.

### Divide/Break
This step involves breaking the problem into smaller sub-problems. Sub-problems should represent a part of the original problem. This step generally takes a recursive approach to divide the problem until no sub-problem is further divisible. At this stage, sub-problems become atomic in nature but still represent some part of the actual problem.

### Conquer/Solve
This step receives a lot of smaller sub-problems to be solved. Generally, at this level, the problems are considered 'solved' on their own.

### Merge/Combine
When the smaller sub-problems are solved, this stage recursively combines them until they formulate a solution of the original problem. This algorithmic approach works recursively and conquer & merge steps works so close that they appear as one.

#### Examples
The following computer algorithms are based on divide-and-conquer programming approach −

*   Merge Sort
*   Quick Sort
*   Binary Search
*   Strassen's Matrix Multiplication
*   Closest pair (points)
*   There are various ways available to solve any computer problem, but the mentioned are a good example of divide and conquer approach.