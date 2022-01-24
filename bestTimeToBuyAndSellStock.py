"""LeetCode - Easy - bestTimeToBuyAndSellStock - Python
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 #left=buy, right=sell
        maxProfit = 0

        while right < len(prices):
            #profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right #always make left min
            right += 1 #always move right down one
        return maxProfit
            
    def __init__(self):
        prices = [7,1,5,3,6,4] #buy at 1, sell at 6
        prices = [2,4,1] #buy at 2, sell at 4
        print(self.maxProfit(prices))
        
"""One Pass
Time complexity: O(n). Only a single pass is needed. Time is going to be linear. We only have to scan through the array one time.
Space complexity: O(1). Only two variables are used. We used a couple of pointers; we didn't need to use an array so space is only O(n). 
Use a left and right pointer; found local min; continue inching right along through the array; maximize profit
"""
