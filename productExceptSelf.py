"""LeetCode - Medium - Product of Array Except Self - Python
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation."""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        output = [1]*len(nums)
        #prefix
        for i in range(len(nums)):
            output[i] = output[i] * p 
            p = p * nums[i] 
        p=1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * p 
            p = p * nums[i] 
        return output
    
    def __init__(self):
        nums = [1,2,3,4]
        print(self.productExceptSelf(nums))
        
"""Prefix and Postfix
Time complexity: O(n) 
Space complexity: O(1). We are not using a prefix array and a postfix array

Make two passes; first in-order; second in reverse, to compute products
"""
