class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def kSum(nums, target, k, start, end):
            result = []
            if k == 2:
                # 2Sum logic
                while start < end:
                    curr_sum = nums[start] + nums[end]
                    if curr_sum == target:
                        result.append([nums[start], nums[end]])
                        while start < end and nums[start] == result[-1][0]:
                            start += 1
                        while start < end and nums[end] == result[-1][1]:
                            end -= 1
                    elif curr_sum < target:
                        start += 1
                    else:
                        end -= 1
            else:
                # kSum logic
                for i in range(start, end + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    sub_results = kSum(nums, target - nums[i], k - 1, i + 1, end)
                    for sub_result in sub_results:
                        result.append([nums[i]] + sub_result)

            return result

        nums.sort()
        return kSum(nums, target, 4, 0, len(nums) - 1)


        