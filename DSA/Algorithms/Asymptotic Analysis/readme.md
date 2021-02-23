Asymptotic analysis of an algorithm refers to defining the mathematical boundation/framing of its run-time performance. Using asymptotic analysis, we can very well conclude the best case, average case, and worst case scenario of an algorithm.

Asymptotic analysis is input bound i.e., if there's no input to the algorithm, it is concluded to work in a constant time. Other than the "input" all other factors are considered constant.

Asymptotic analysis refers to computing the running time of any operation in mathematical units of computation. For example, the running time of one operation is computed as f(n) and may be for another operation it is computed as g(n2). This means the first operation running time will increase linearly with the increase in n and the running time of the second operation will increase exponentially when n increases. Similarly, the running time of both operations will be nearly the same if n is significantly small.

Usually, the time required by an algorithm falls under three types −

  * Best Case − Minimum time required for program execution.

  * Average Case − Average time required for program execution.

  * Worst Case − Maximum time required for program execution.

Asymptotic Notations
Following are the commonly used asymptotic notations to calculate the running time complexity of an algorithm.

  * Ο Notation
  * Ω Notation
  * θ Notation


## Big Oh Notation, Ο
The notation Ο(n) is the formal way to express the upper bound of an algorithm's running time. It measures the worst case time complexity or the longest amount of time an algorithm can possibly take to complete.

<p align="center">
  <img src="https://www.tutorialspoint.com/data_structures_algorithms/images/big_o_notation.jpg">
</p>

For example, for a function f(n)

    Ο(f(n)) = { g(n) : there exists c > 0 and n0 such that f(n) ≤ c.g(n) for all n > n0. }

## Omega Notation, Ω
The notation Ω(n) is the formal way to express the lower bound of an algorithm's running time. It measures the best case time complexity or the best amount of time an algorithm can possibly take to complete.

<p align="center">
  <img src="https://www.tutorialspoint.com/data_structures_algorithms/images/omega_notation.jpg">
</p>

For example, for a function f(n)

    Ω(f(n)) ≥ { g(n) : there exists c > 0 and n0 such that g(n) ≤ c.f(n) for all n > n0. }

## Theta Notation, θ
The notation θ(n) is the formal way to express both the lower bound and the upper bound of an algorithm's running time. It is represented as follows 

<p align="center">
  <img src="https://www.tutorialspoint.com/data_structures_algorithms/images/theta_notation.jpg">
</p>