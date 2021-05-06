#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex):
            res.append(1)
            for j in range(i,0,-1):
                res[j]+=res[j-1]
        res.append(1)
        return res
        
# @lc code=end

