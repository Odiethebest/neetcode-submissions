class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 获取网格的行数和列数
        R, C = len(grid), len(grid[0])
        
        # 初始化队列，存储所有腐烂橙子的初始位置和时间
        q = deque()
        # 统计新鲜橙子的数量
        fresh = 0
        
        # 第一次遍历：找出所有腐烂橙子和新鲜橙子
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    # 腐烂橙子加入队列，初始时间为0
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    # 统计新鲜橙子数量
                    fresh += 1
        
        # 如果没有新鲜橙子，直接返回0
        if fresh == 0: 
            return 0
        
        # 初始化访问集合，标记已处理的橙子位置（包括所有腐烂橙子）
        visit = set((r, c) for r, c, t in q)
        # 定义四个方向：下、右、上、左
        direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # 记录最大花费的时间
        max_time = 0
        
        # BFS遍历：模拟腐烂过程
        while q:
            # 取出队列前端的橙子及其腐烂时间
            r, c, time = q.popleft()
            # 更新最大时间
            max_time = max(max_time, time)
            
            # 检查四个相邻方向
            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                
                # 检查新位置是否有效、是否是新鲜橙子、是否未访问过
                if (0 <= nr < R 
                and 0 <= nc < C 
                and grid[nr][nc] == 1 
                and (nr, nc) not in visit):
                    # 新鲜橙子变腐烂，加入队列（时间+1）
                    q.append((nr, nc, time + 1))
                    # 标记为已访问
                    visit.add((nr, nc))
                    # 新鲜橙子数量-1
                    fresh -= 1
        
        # 如果还有新鲜橙子未腐烂，返回-1；否则返回最大时间
        return max_time if fresh == 0 else -1