class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, ans = 0, len(height) - 1, 0
        while l < r:
            t = min(height[l], height[r])
            while height[l] <= t and l < r:
                ans += t - height[l]
                l += 1
            while height[r] <= t and l < r:
                ans += t - height[r]
                r -= 1
        return ans
        