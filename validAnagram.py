"""LeetCode - Easy - validAnagram - Python
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once."""

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] =  1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS: 
            if countS[c] != countT.get(c,0): 
                return False
        return True
    
        #return Counter(s) == Counter(t) - too easy, might not count
    
        #Sorted
        return sorted(s) == sorted(t) 
    
    def __init__(self):
        s = "anagram"
        t = "nagaram"
        print(self.isAnagram(s,t)) #true
        
"""Sort and Dictionary
Time complexity: O(n) or O(s+t). We have to iterate through both strings.
Space complexity: O(s + t ). building hashmaps of size of s and size of t
first, check the length (should be equal). Second, create two hashmaps: keys(letters) and values(frequencies)
instead of countS[s[i]] = 1 + countS[s[i]], use
countS[s[i]] = i + countS.get(s[i], 0) just in case the key is not already in the hashmap
Third, after building the two hashmaps, iterate thru one of them & check to make sure the values (frequencies) of each letter are the same
For sorted: if you sort the two strings, they should be identical

"""
