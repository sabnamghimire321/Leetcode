from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows, cols = len(seats), len(seats[0])
     
        def valid_masks(row):
            broken = sum(1 << c for c in range(cols) if seats[row][c] == '#')
            result = []
            for mask in range(1 << cols):
                if mask & broken:
                    continue
                if mask & (mask << 1):  
                    continue
                result.append(mask)
            return result
     
        prev_row_options = {0: 0}  
     
        for row in range(rows):
            curr_row_options = {}
            for mask in valid_masks(row):
                best_for_mask = 0
                for prev_mask, prev_count in prev_row_options.items():
                    if (mask & (prev_mask << 1)) or (mask & (prev_mask >> 1)):
                        continue  
                    best_for_mask = max(best_for_mask, prev_count)
                popcount = bin(mask).count('1')
                curr_row_options[mask] = best_for_mask + popcount
            prev_row_options = curr_row_options
     
        return max(prev_row_options.values()) if prev_row_options else 0
