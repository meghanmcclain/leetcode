"""LeetCode - Easy - longestCommonPrefix - Python
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        maxPrefix = ""
        for i, j in zip(strs[0], strs[-1]):
            if i == j: 
                maxPrefix += i
            else:
                break
                
        return maxPrefix
    
    def __init__(self):
        strs = ["flower", "flow", "flight"]
        print(self.longestCommonPrefix(strs))
        
 """Notes: zip() function - the first item in each passed iterator is paired together, 
 and then the second item is paired together etc.
 sort() function - sorts the list alphabetically
 """
