#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
# 1D DP 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [0]*len(nums)
        res[0]=nums[0]
        for i in range(1,len(nums)):
            res[i] = max(nums[i],res[i-1]+nums[i])
        return max(res)
        
# @lc code=end

