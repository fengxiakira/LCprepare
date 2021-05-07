# return the last -3 index linkedlist node val
# microsoft
# 快慢指针比的不是速度，是指针前后的位置，快慢指针都是同时出发的
def last3val(self,head:node)->int:
    if not head or not head.next or not head.next.next:
         return 0
    slow = head
    fast = head.next.next
    while fast:
          fast = fast.next
          slow = slow.next
    return slow.val

[]
[1]
[1,2]
[1,2,3,4]
[1,2,3,4,5]
[1,2,3,4,5,6,7,8]