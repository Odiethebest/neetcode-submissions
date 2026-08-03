class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        
        count = 0
        last_end = float('-inf')
        
        for start, end in intervals:
            if start >= last_end:
                count += 1
                last_end = end
        
        return n - count