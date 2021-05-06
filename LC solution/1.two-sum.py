#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

# hash map  value(key): index(value)
# 目的是要找到left剩下的位置
"""
for count, item in enumerate(grocery):
  print(count, item)

OutPut:
0 bread
1 milk
2 butter
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digits = {}
        for i , value in enumerate(nums):
            left = target - nums[i]
            if left in digits:
                return [i,digits[left]]
            else:
                digits[value]=i
        
# @lc code=end

