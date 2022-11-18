# 

##how to come up with the structure

### SRTBOT

* subproblem
* relation
* topological order
* base case
* original problem
* time

####Example 1 merge sort(A)
* subproblem

  s(i,j) = sorted array on A[i:j]
* relation

  s(i,j) = merge(s(i,m),s(m,j)) while m = (i+j)/2

* topological order

  increasing j -i

* base case

  s(i,j) = []
* original problem 
  
  s(0,n)
* time
  
  T（n） = 2T(n/2) + O(n) = O(nlgn)

####Example 2 Fibonacci number: given n, compute Fn

Fn = Fn-1 + Fn-2, F1 = F2 = 1

* subproblem
    
    F(i), 1< = i < = n

* relation

    F(i) = F(i-1) + F(i-2)

* topological order
    
    increasing i, for i  = 1,2,...,n

* base case
    
    F(1) = F(2) = 1
* original problem

    F(n)
* time
    T(n) = T(n-1) + T(n-2) + 1

#### Fibonacci number + memoization
remember and reused some solutions to sub-problems
* maintain dictionary mapping sub-problems to solutions
* recursive function returns stored value or if does not exist, compute and store it.









