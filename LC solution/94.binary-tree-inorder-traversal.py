#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
            res = []
                
            def inorderHelper(root):
                if not root:
                    return
                # if root.left:
                inorderHelper(root.left)
                res.append(root.val)
                # if root.right:
                inorderHelper(root.right)
                    
            inorderHelper(root)
            
                
            return res
        
# @lc code=end

