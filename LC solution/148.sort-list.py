# @before-stub-for-debug-begin
from python3problem148 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

"""
Quick Sort : 
TC: O(NLOGN)
SC: O(1)

"""

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:


        # define pivot
        def partition(start,end):
            i = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            # if 2 pivot are same value
            pivotPost = pivotPrev
            while i != end:
                if i.val > pivotPrev.val:
                    # to pivot right
                    i.next = pivotPost.next
                    pivotPost.next = i
                elif i.val < pivotPrev.val:
                    # to pivot left
                    i.next = pivotPrev
                    start.next = i
                else:
                    i.next = pivotPost.next
                    pivotPost.next = i
                    pivotPost = pivotPost.next

                i = i.next
            return [pivotPrev,pivotPost]

        def quickSort(start,end):
            if start.next != end:
                prev,post = partition(start,end)
                quickSort(start,prev)
                quickSort(post,end)

        new_head = ListNode(0)
        new_head.next = head
        quickSort(new_head,None) 
        return new_head.next    


        
# @lc code=end

