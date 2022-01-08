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
