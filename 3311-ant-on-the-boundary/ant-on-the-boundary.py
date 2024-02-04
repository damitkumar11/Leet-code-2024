from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        position = 0
        
        for num in nums:
            if num > 0:
                position += num
            elif num < 0:
                position += num
            # Check if the ant is on the boundary after moving
            if position == 0:
                count += 1
        
        return count
        