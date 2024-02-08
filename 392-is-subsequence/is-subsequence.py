class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers for both strings
        s_ptr = 0
        t_ptr = 0
        
        # Iterate through both strings
        while s_ptr < len(s) and t_ptr < len(t):
            # If characters match, move pointer for s
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            # Always move pointer for t
            t_ptr += 1
        
        # If s_ptr reached the end of s, it means s is a subsequence of t
        return s_ptr == len(s)
        