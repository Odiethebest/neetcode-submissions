class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if node is None:
                return False

            current_sum += node.val

            if node.left is None and node.right is None:
                return current_sum == targetSum

            if dfs(node.left, current_sum):
                return True

            if dfs(node.right, current_sum):
                return True

            return False

        return dfs(root, 0)