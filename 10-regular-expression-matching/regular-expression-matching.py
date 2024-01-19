class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Create a 2D dp array to store matching results
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty pattern matches empty string

        # Fill in the first row for patterns with '*'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill in the dp array
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return dp[len(s)][len(p)]
        