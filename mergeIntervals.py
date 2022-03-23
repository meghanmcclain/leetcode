"""LeetCode - Medium - Merge Intervals - Python
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input."""    
  
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0]) #1, 2, 3, 4
        output = [intervals[0]]
        
        for start, end in intervals[1:]: #5
            lastEnd = output[-1][1] #6
            
            if start <= lastEnd: #7
                output[-1][1] = max(lastEnd, end) #8
            else: #9
                output.append([start,end])
        return output
    
  def __init__(self):
        intervals = [[1,3], [2,6], [8,10], [15,18]]
        print(self.merge(intervals))
        
"""Sort the array based on start value, iterate through intervals, check if current start <= lastEnd (if it is, merge & update end value)
#1: O(nLogn) - sorting a list of size n using sort() function
#2: lambda arguments : expression
#3: sorting a list of pairs, sort by start value i[0]
#4: initialize to first interval to avoid edge case
#5: iterate through every interval
#6: from output, get end value of most recent interval
#7: if current start is <= lastEnd value, merge
#8: update current end value with the highest number, we want [1,5], [2, 4] = [1,5] (not [1,4])
#9: if current interval doesn't overlap with previous interval, add it to output
"""
