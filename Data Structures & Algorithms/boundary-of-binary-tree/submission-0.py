class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_boundary, right_boundary, leaves = [], [], []
        self.preorder(root, left_boundary, right_boundary, leaves, 0)
        left_boundary.extend(leaves)
        left_boundary.extend(right_boundary)
        return left_boundary

    def is_leaf(self, cur):
        return cur.left is None and cur.right is None

    def is_right_boundary(self, flag):
        return flag == 2

    def is_left_boundary(self, flag):
        return flag == 1

    def is_root(self, flag):
        return flag == 0

    def left_child_flag(self, cur, flag):
        if self.is_left_boundary(flag) or self.is_root(flag):
            return 1
        elif self.is_right_boundary(flag) and cur.right is None:
            return 2
        else:
            return 3

    def right_child_flag(self, cur, flag):
        if self.is_right_boundary(flag) or self.is_root(flag):
            return 2
        elif self.is_left_boundary(flag) and cur.left is None:
            return 1
        else:
            return 3

    def preorder(self, cur, left_boundary, right_boundary, leaves, flag):
        if cur is None:
            return

        if self.is_right_boundary(flag):
            right_boundary.insert(0, cur.val)
        elif self.is_left_boundary(flag) or self.is_root(flag):
            left_boundary.append(cur.val)
        elif self.is_leaf(cur):
            leaves.append(cur.val)

        self.preorder(cur.left, left_boundary, right_boundary, leaves, self.left_child_flag(cur, flag))
        self.preorder(cur.right, left_boundary, right_boundary, leaves, self.right_child_flag(cur, flag))