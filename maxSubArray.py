"""LeetCode - Easy - Maximum Subarray - Python
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array."""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = -math.inf
        maxSum = -math.inf 
        for i in range(len(nums)):
            currentSum = max(nums[i],currentSum + nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum
    
    def __init__(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        print(self.maxSubArray(nums))
        
"""Kadane's Algorithm
Time Complexity: O(n) where n is the size of the array
Space Complexity: O(1)

-iterate once through list
-compare current number with the currentSum+current number
-if the current number is greater than the current sum+current number, then update 
the currentSum to the current number (forget all the numbers before it)
compare max with currentSum & update max if necessary
"""
