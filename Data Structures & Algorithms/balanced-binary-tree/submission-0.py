class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 1. 修复你的深度函数：让它返回真实的深度（高度）
        def TreeDepth(node):
            if not node:
                return 0
            leftDepth = TreeDepth(node.left)
            rightDepth = TreeDepth(node.right)
            # 公式死记硬背：真实深度 = 左右较深的那边 + 1
            return max(leftDepth, rightDepth) + 1
            
        # 2. 主函数逻辑修复
        if not root:
            return True  # 空树默认是平衡的
            
        # 算一下当前节点左边和右边的真实深度
        left = TreeDepth(root.left)
        right = TreeDepth(root.right)
        
        # 满足三个条件才算真正的平衡：
        # 条件一：我当前节点的左右差值 <= 1
        # 条件二：我的左子树内部也必须是平衡的（递归检查）
        # 条件三：我的右子树内部也必须是平衡的（递归检查）
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)