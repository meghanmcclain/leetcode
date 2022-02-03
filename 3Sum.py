"""LeetCode - Medium - 3Sum - Python
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets."""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [] #list of lists
        for i, v in enumerate(nums): 
            if i > 0 and v == nums[i-1]: #prevent duplicates
                continue
            l, r = i+1, len(nums)-1 #twoSumII
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([v, nums[l], nums[r]])
                    l += 1 #only have to update 1 pointer, conditions above will update the other
                    while nums[l] == nums[l-1] and l < r: #if duplicate
                        l += 1 #keep shifting pointer
        return result
    
    def __init__(self):
        nums = [-1,0,1,2,-1,-4]
        print(self.threeSum(nums))
        
"""Sort the Array, Prevent Duplicates, Use a Left & Right Pointer - Similar to TwoSum II
Time Complexity: O(n^2) - two nested loops 
O(n log n) [sorting the array] + O(n^2) [using 1 loop to tell us the first value v, & second loop to solve TwoSum]
Space Complexity: O(1) or O(n) [sorting does take extra memory in some libraries]
"""
