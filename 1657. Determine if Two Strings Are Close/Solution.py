from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # Check if the lengths of the words are different
        if len(word1) != len(word2):
            return False
        
        # Count the occurrences of characters in both words
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Check if the sets of characters are the same
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        # Check if the sets of character frequencies are the same
        if set(count1.values()) != set(count2.values()):
            return False
        
        # Check if the sorted character frequencies are the same
        return sorted(count1.values()) == sorted(count2.values())
