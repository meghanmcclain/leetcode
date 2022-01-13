"""LeetCode - Easy - validParentheses - Python
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid..
"""

class Solution:
    def isValid(self, s: str) -> bool:
        #one way using pop() function
        stack = []
        dict = {"]":"[","}":"{",")":"("}
        for i in s:
            if i in dict.values(): #openers
                stack.append(i)
            elif i in dict.keys(): #closers
                if stack == [] or dict[i] != stack.pop(): #1
                    return False
            else:
                return False
        return stack == []
    
        #concise code - better way
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
    
        #another way
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]: #2
                stack.pop() #3
            else:
                return False
        return stack == []
    
    def __init__(self):
        #s = "(]"
        s = "{[()[({})]]}"
        print(self.isValid(s))

"""Notes: Python's built-in data structure list can be used as a stack. Instead of push(), append() is used to add elements to the top of the stack while pop() removes the element in LIFO order.

#1: if you get a closer & the stack is empty, return False (your string is starting with a closer).
If you get a closer, then the opener better be the last one added on the stack. If not, return False.

#2: if you get a closer, then the last one on the stack better be an opener

#3: remove the last one on stack(opener)
 """
