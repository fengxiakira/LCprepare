#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Deletion Cost to Avoid Repeating Letters
#
# python 2D array use
# @lc code=start
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s = list(s)
        queue = [[s[0], cost[0]]]
  # iterarte through queue
  # add to the queue if it is not the same char
  # if it is the  same char, compare the cost,update 
  # the cost of the last item in the queue
        res = 0
        for i in range(1, len(s)):
            if queue[-1][0] != s[i]:
                queue.append([s[i],cost[i]])
            else:
      # if cost[i] < cost[queue[-1]]
                if cost[i] < queue[-1][1]:
                    res += cost[i]        
                else:
                    res += queue[-1][1]    
                    queue[-1][1] = cost[i]
        return res
        
# @lc code=end

