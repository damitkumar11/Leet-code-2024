# DFS
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        self._combinationSum(target, candidates, [], ans)
        return ans

    def _combinationSum(self, target, candidates, cur, ans):
        if target == 0:
            ans.append(cur[:])
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            self._combinationSum(target - candidates[i], candidates[i:],
                                 cur + [candidates[i]], ans)
        