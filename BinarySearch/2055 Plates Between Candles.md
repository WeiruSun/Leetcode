# 2055. Plates Between Candles

There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.


**Solution**
input:

queries : list contain two index

s: list contains * and |

needed output:

## a stupid solution ->TLE

use the most simple way, get the index of candles in list, find the sublist by given queries, and calculate the difference of index
 ```
 class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        candle_list = []
        for i in range(0,len(s)):
            if s[i]== "|":
                candle_list.append(i)
        
        if len(candle_list) <=1:
            return 0
        
        for i in range(0,len(queries)):
            count = self.helper(candle_list,queries[i][0],queries[i][1])
            res.append(count)
        return res
            
    def helper(self,candle_list,left,right):
        sublist = []
        subcount = 0
        for i in range(0,len(candle_list)):
            if candle_list[i]>=left and candle_list[i] <= right:
                sublist.append(candle_list[i])
        
        if len(sublist) <=1:
            return subcount
        else:
            for j in range(1, len(sublist)):
                subcount += (sublist[j] - sublist[j-1])-1
            return subcount      
```



