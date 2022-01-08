"""LeetCode - romanToInt - Easy - Python
Given a roman numeral, convert it to an integer.
"""

#My Preferred Approach #2: Left-to-Right Pass Improved
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40, 
    "XC": 90,
    "CD": 400,
    "CM": 900
}
#Approach #1: Left-to-Right Pass
#Approach #3: Right-to-Left Pass
"""values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}"""

class Solution:
    def romanToInt(self, s: str) -> int:
        #My Preferred Approach #2
        total = 0
        i = 0
        while i < len(s):
            # This is the subtractive case.
            if i < len(s) - 1 and s[i:i+2] in values: 
                total += values[s[i:i+2]] 
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total
      
      #Approach #1
        """total = 0
        i = 0
        while i < len(s):
            #if this is the subtractive case
            #if smaller valued symbol is before a larger valued symbol
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]: 
                total += values[s[i+1]] - values[s[i]] #add the difference of the next 2 symbols
                i += 2 #go forward 2 places
            #else this is NOT the subtractive case
            else:
                total += values[s[i]] #add the current symbol &...
                i += 1 #...go forward 1 place
        return total"""
        #Approach #3: Right-to-Left Pass
        """total = values.get(s[-1]) #start at end, initialize sum here, 5
        for i in reversed(range(len(s) - 1)): #work backwards thru string
            if values[s[i]] < values[s[i + 1]]: #1 < 5, 10<50
                total -= values[s[i]] #5-1=4, 54-10=44
            else: #50 > 1,
                total += values[s[i]] #54
        return total"""
    
    def __init__(self):
        s = "MCMXCIV"
        print(self.romanToInt(s))
        
"""Complexity Analysis
Time complexity : O(1)
Space complexity : O(1)
"""
        
