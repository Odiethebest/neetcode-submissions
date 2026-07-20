class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 使用集合来追踪已占用的列和对角线
        # 这样可以在 O(1) 时间内检查冲突，比遍历整个棋盘高效
        col = set()           # 存储已放置皇后的列号
        posDiag = set()       # 存储正对角线（↗ 方向）：r + c 为常数
        negDiag = set()       # 存储负对角线（↖ 方向）：r - c 为常数

        res = []              # 存储所有有效的解
        board = [["."] * n for i in range(n)]  # 初始化空棋盘

        def backtrack(r):
            # 边界条件：已经在所有 n 行都放置了皇后
            if r == n:
                # 将每一行（列表）转换为字符串，并将此解加入结果
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # 尝试在当前行的每一列放置皇后
            for c in range(n):
                # 检查位置 (r, c) 是否与现有皇后冲突：
                # c in col: 该列已有皇后
                # (r + c) in posDiag: 该正对角线已有皇后
                # (r - c) in negDiag: 该负对角线已有皇后
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue  # 跳过此列，尝试下一列
                
                # ===== 做出选择：在 (r, c) 放置皇后 =====
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # ===== 递归：继续在下一行放置皇后 =====
                backtrack(r + 1)

                # ===== 撤销选择（回溯）=====
                # 移除皇后并恢复所有状态，以便尝试当前行的其他列
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        # 从第 0 行开始回溯
        backtrack(0)
        return res