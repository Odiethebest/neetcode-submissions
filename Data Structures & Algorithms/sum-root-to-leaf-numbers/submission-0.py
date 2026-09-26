# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(root, 0)])
        while q:
            cur, num = q.popleft()
            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                res += num
                continue
            if cur.left:
                q.append((cur.left, num))
            if cur.right:
                q.append((cur.right, num))
        return res