# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while curr:
            if curr.val < val:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right
            if curr.val > val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left
        return root
