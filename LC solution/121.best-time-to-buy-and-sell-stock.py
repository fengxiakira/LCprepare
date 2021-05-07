#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
# find min value and record max profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = math.inf 
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            max_profit = max(max_profit, prices[i]-min_val)

        return max_profit


        
# @lc code=end

