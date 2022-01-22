"""LeetCode - Easy - containsDuplicate - Python
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct."""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set() #no duplicates, no key-value pairs (don't care about indices)
        for i in nums: #don't need range
            if i in hashSet:
                return True
            hashSet.add(i)
        return False
            
    def __init__(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        print(self.containsDuplicate(nums))
        
"""One-Pass Hash Set
We want to use a hash set (instead of a hashmap) because there are not duplicates in a set and we don't care about indices so we don't need the key-value pairs.
Using the functions set() and add() to create the hashset and add items to the hash set.
We can do this in one-pass. While we are iterating and inserting elements into the hash set, 
we also look to check if current element is already in the hash set. 
If it exists, we have found a solution and return True immediately.
Time complexity: O(n). We traverse the list containing n elements only once. Each lookup in the table costs only O(1) time.
Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores at most n elements."""
