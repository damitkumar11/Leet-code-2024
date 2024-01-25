# DFS
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        self._combinationSum2(target, candidates, [], ans)
        return ans

    def _combinationSum2(self, target, candidates, cur, ans):
        if target == 0:
            ans.append(cur[:])
            return
        i = 0
        while i < len(candidates):
            if candidates[i] > target:
                break
            self._combinationSum2(target - candidates[i], candidates[i + 1:],
                                  cur + [candidates[i]], ans)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            i += 1