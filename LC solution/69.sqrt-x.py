#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
# binary serach
class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x
        while start <= end:
            mid = start + (end - start)//2
            if mid * mid < x:
                start += 1
            else:
                end -= 1
        return end
        
# @lc code=end

