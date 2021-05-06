# @before-stub-for-debug-begin
from python3problem2 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = 0
        dummy = tail = ListNode(0)
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(s%10)
            tail = tail.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        
# @lc code=end

