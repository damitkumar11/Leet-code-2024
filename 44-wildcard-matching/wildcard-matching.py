# Dynamic programming
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ans = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        ans[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                ans[0][i] = ans[0][i - 1]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "*":
                    ans[i][j] = ans[i - 1][j] or ans[i][j - 1]
                elif p[j - 1] == "?":
                    ans[i][j] = ans[i - 1][j - 1]
                else:
                    ans[i][j] = (s[i - 1] == p[j - 1]) and ans[i - 1][j - 1]
        return ans[-1][-1]
        