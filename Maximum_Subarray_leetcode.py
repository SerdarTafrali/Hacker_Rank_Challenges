"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = float("-inf"),0
        
        for n in nums:
            cur_sum = max(cur_sum+n,n)
            max_sum = max(cur_sum,max_sum)
            
        return max_sum
     
