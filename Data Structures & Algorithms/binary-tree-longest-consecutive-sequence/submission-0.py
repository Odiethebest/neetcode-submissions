class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        self.dfs(root, None, 0)
        return self.max_length
    
    def dfs(self, p, parent, length) -> None:
        if p is None:
            return
        
        if parent is not None and p.val == parent.val + 1:
            length = length + 1 
        else:
            length = 1
        self.max_length = max(self.max_length, length)
        self.dfs(p.left, p, length)
        self.dfs(p.right, p, length)