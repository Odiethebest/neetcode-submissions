# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []                  # 准备一个空篮子，装当前这一层的所有数值
            for i in range(qLen):       # 严格按照刚才拍的快照人数，处理这么多次
                node = q.popleft()      # 1. 把排在最前面的人请出队伍
                if node:                # 2. 如果这人真实存在（不是 None）
                    level.append(node.val)  # (1) 收集他的值
                    q.append(node.left)     # (2) 让他的左孩子去队伍最后面排队
                    q.append(node.right)    # (3) 让他的右孩子去队伍最后面排队
            if level:
                res.append(level)
                #结算当前层，交差
        return res







