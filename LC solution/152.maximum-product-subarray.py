#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        max_prod=nums[0]
        min_prod=nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            next_max = max_prod*nums[i]
            next_min = min_prod*nums[i]
            max_prod = max(nums[i],max(next_max,next_min))
            min_prod = min(nums[i],min(next_max,next_min))
            res = max(res,max_prod)
        return res
# @lc code=end

