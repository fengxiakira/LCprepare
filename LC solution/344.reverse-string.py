#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start,end = 0, len(s)-1
        while start < end:
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
        
# @lc code=end

