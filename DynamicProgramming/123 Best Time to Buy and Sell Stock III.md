#  Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

```
 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxTime = 2
        n = len(prices)
        dp = [[[0 for i in range(2)]for j in range(maxTime+1)]for k in range(n)]
        for i in range(n):
            for k in range(maxTime,0,-1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0]= max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
            
        return dp[n-1][maxTime][0]
```

