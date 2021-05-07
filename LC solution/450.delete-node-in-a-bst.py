#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return

        def findNode(root,key): 
            if not root:
                return
            if root.val ==  key:
                return root
            left = findNode(root.left,key)
            right = findNode(root.right,key)
            if not left:
                return right
            if not right:
                return left
            return root

        res = findNode(root,key)
        res.left = res.left.left
        # delete ? 

        return res

                

        
        
        
# @lc code=end

