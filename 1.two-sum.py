"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List

# solution 1 brute force
"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums:
                if i + j == target:
                    return [i, j]"""

list = [3, 2, 4]
for index, item in enumerate(list, start=0):  # default is zero
    print(index, item)


class Solution:
    def twoSum_bruteforce_enumerate(self, nums: List[int], target: int) -> List[int]:
        for index1, item1 in enumerate(nums):
            for index2, item2 in enumerate(nums):
                if item1 + item2 == target:
                    return [index1, index2]

    def twoSum_bruteforce_range(self, nums: List[int], target: int) -> List[int]:
        """Runtime: 6140 ms, faster than 10.28 % of Python3 online submission for Two Sum.
            Memory Usage: 14.9 MB, less than 95.03 % of Python3 online submissions for Two Sum."""
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):  # range here ensure the index are not the same
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_bruteforce_range1(self, nums: List[int], target: int) -> List[int]:
        """Runtime: 6140 ms, faster than 10.28 % of Python3 online submission for Two Sum.
            Memory Usage: 14.9 MB, less than 95.03 % of Python3 online submissions for Two Sum."""
        for i in range(0, len(nums) - 1):
            for j in range(0, len(nums) - 1):  # range here ensure the index are not the same
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]




answer = Solution()
print(answer.twoSum_bruteforce_range1(list, 6))
