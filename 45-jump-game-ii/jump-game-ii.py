# Greedy
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0 # number of jumps
        cur1 = 0 # maximum jump length (current number of jumps)
        cur2 = 0 # maximum jump length (current point)
        for i in range(len(nums)):
            if cur1 < i:
                cur1 = cur2
                ans += 1
            cur2 = max(cur2, i + nums[i])
        return ans
        