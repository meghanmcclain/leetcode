"""LeetCode - Easy - TwoSum - Python
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	    hashmap = {}
	    for i in range(len(nums)):
		    complement = target - nums[i]
		    if complement in hashmap:
			    return [i, hashmap[complement]]
		    hashmap[nums[i]] = i

    def __init__(self):
	    nums = [2,7,11,15]
	    target = 9
	    print(self.twoSum(nums, target))
		
"""One-Pass Hash Table
It turns out we can do it in one-pass. While we are iterating and inserting elements into the hash table, 
we also look back to check if current element's complement already exists in the hash table. 
If it exists, we have found a solution and return the indices immediately.

Time complexity: O(n). We traverse the list containing n elements only once. Each lookup in the table costs only O(1) time.
Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements."""
