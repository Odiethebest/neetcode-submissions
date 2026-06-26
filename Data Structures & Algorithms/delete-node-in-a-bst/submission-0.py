class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1. 找不到要删的节点，直接返回
        if not root:
            return None
            
        # 2. 去找目标节点
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        # 3. 找到了目标节点！(key == root.val) 开始处理离职手续
        else:
            # 情况 1 & 2：只有 0 个 或 1 个孩子
            # 如果左边是空的，直接把右孩子交上去（如果右边也是空的，刚好交上去 None，涵盖了情况 1）
            if not root.left:
                return root.right
            # 如果右边是空的，直接把左孩子交上去
            elif not root.right:
                return root.left
                
            # 情况 3：有 2 个孩子。去右子树找“替身”（最小值）
            curr = root.right
            while curr.left:
                curr = curr.left
                
            # 偷天换日：把替身的值覆盖到当前离职节点上
            root.val = curr.val
            
            # 斩草除根：去右子树里，把那个替身节点删掉
            root.right = self.deleteNode(root.right, root.val)
            
        return root