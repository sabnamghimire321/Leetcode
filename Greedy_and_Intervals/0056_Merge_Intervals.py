from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            last = result[-1]
            
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                result.append([start, end])
                
        return result
