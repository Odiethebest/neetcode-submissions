# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))
    

    def sameTree(self, root, subRoot) -> bool:
        # 两棵树都为空，说明匹配成功
        if not root and not subRoot:
            return True

        # 只有一个为空，说明结构不同，匹配失败
        if not root or not subRoot:
            return False

        # 当前节点值不同，匹配失败
        if root.val != subRoot.val:
            return False

        # 当前节点值相同，继续比较左右子树
        left_same = self.sameTree(root.left, subRoot.left)
        right_same = self.sameTree(root.right, subRoot.right)

        return left_same and right_same





