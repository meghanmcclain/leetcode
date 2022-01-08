"""LeetCode - Easy - isPalindrome - Python
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
"""

class Solution:
  def isPalindrome(self, x: int) -> bool:
	    #Not using strings
	    temp = x
	    rev = 0
	    while x > 0:
		    dig = x%10 #8, 3, 1 get far right digit
		    rev = rev*10+dig #8, 83, 831
		    x=x//10 #13, 1, 
	    if temp == rev:
		    return True
	    else:
		    return False
        
      #Using strings
	    return str(x) == str(x)[::-1]
        
      def __init__(self):
        x = 138
        print(self.isPalindrome(x))
        
"""Algorithm Complexity
Time complexity : O(log(n)). We divided the input by 10 for every iteration, so the time complexity is O(log(n))
Space complexity : O(1)
"""
