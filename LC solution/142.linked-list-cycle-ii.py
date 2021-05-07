#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # detect cycle,2 pointer
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next   
            if slow == fast:
                break
        # no cycle return none pointer
        if not fast or not fast.next:
            return None
        # reset slow to head, fast is at meet point, run them at same pace
        # fast比slow多走了k步
        # slow从头开始走k-m步。fast还剩下k-m步要走。当slow == fast时，跳出循环,这时slow正好在环起点
        slow = head
        while slow!=fast:
            fast = fast.next
            slow = slow.next
            
        return slow
        
# @lc code=end

