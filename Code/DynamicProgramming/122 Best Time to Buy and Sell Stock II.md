# Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 ```
 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        
        dp = [[0 for i in range(2)]for j in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1,n):
            temp = dp[i-1][0]
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+ prices[i])
            dp[i][1] = max(dp[i-1][1],temp-prices[i])
        return dp[n-1][0]
 
```

example:

prices = [7,1,5,3,6,4]
not hold  hold
dp temp [][]        [][]    
0   0     0          -7      
1   0  max(0,-7+1)= 0  max(-7,0-1) =-1
2   0  max(0, -1+5)=4  max(-1,0-5) = -1
3   4  

