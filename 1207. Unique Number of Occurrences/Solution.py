from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Count occurrences of each value in the array
        counts = Counter(arr)
        
        # Check if the counts are unique
        return len(counts.values()) == len(set(counts.values()))
