# Dynamic Programming

## 实质
dynamic programming的programming不是指编程，而是数学上的一种解决优化问题的方法，叫做列表法(tabular method)，大致过程是将函数的不同变量值在表中列出并对表进行各种操作来求得结果。

如果列表法是静态（static）的，则动态规划算法中，表格是慢慢增长的，先解决相对简单的子问题，然后通过子问题的结合求取父问题，这样表格好像是“动态”的。


##动态规划定义
- 把原问题分解为相对简单的子问题的方式求解复杂问题的方法。
- 一旦某个给定子问题的解已经算出，则将其记忆化存储，以便下次需要同一个子问题解之时直接查表。 
- 动态规划问题存在重叠子问题，具备最优子结构，使用状态转移方程进行穷举
- 状态转移方程需考虑：
  - base case 
  - 问题状态
  - 对于每个状态的选择
  - 如何表现状态和选择 （dp数组的定义）

## Memoization vs. Tabulation 简介
动态规划通常有两种解法：top-down和bottom-up。

**top-down**

通常以递归形式出现，从父问题开始，递归地求解子问题。top-down的求解过程通常与memoization结合，即将计算过的结果缓存在数组或者哈希表等结构中。当进入递归求解问题时，先查看缓存中是否已有结果，如果有则直接返回缓存的结果。

**bottom-up**

通常以循环形式出现。bottom-up的求解过程通常与tabulation结合，即先解最小的子问题，解决后将结果记录在表格中（通常是一维或二维数组），解决父问题时直接查表拿到子问题的结果，然后将父问题的结果也填在表中，直到把表格填满，最后填入的就是起始问题的结果。



###例题：509. Computing Fibonacci Numbers

本问题没有求最值，用来学习状态转移方程
```python
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
```
####solution 1 ： 暴力递归
```Python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1 or n == 2 :
            return 1
        return self.fib(n-1) + self.fib(n-2)
```
时间复杂度： O(2**n)

子问题时间复杂度： O(1)

问题： 大量重复计算




#### solution 2 : recursion with notebook
递归树剪枝
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: 
            return 0
        memo = [0] * (n+1)
        return self.helper(memo,n)

    def helper(self,memo,n):
        #base case
        if n == 1 or n == 2:
            return 1
        if memo[n] != 0:
            return memo[n]
        memo[n] = self.helper(memo,n-1) + self.helper(memo,n-2)
        return memo[n]
```
时间复杂度： O(n)


#### bottom-up
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        memo = [0] * (n+1)

        #base case
        memo[1] = memo[2] = 1
        for i in range(3, n + 1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
```

#### bottom-up + 状态压缩
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        prev = 1
        prevp = 1

        for i in range(3, n + 1):
            cur = prev + prevp
            prevp = prev
            prev = cur
        return cur
```