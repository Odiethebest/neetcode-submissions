class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        N = len(grid)
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 上下左右四个方向
        
        # =================== 阶段1: DFS找第一个岛屿 ===================
        
        # 遍历整个网格找到第一块陆地
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    # 找到第一个岛屿，用DFS标记所有连接的陆地
                    q1 = deque([(r, c)])
                    q2 = deque([(r, c)])  # 初始化 q2 以存储 BFS 起点
                    grid[r][c] = 2  # 标记为2，表示已访问的第一个岛屿
                    
                    # DFS: 展开所有连接的陆地
                    while q1:
                        x, y = q1.popleft()
                        
                        # 检查四个相邻格子
                        for dx, dy in direct:
                            nx, ny = x + dx, y + dy
                            # 如果相邻格子是陆地(1)，标记为2并加入DFS队列
                            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                                grid[nx][ny] = 2
                                q1.append((nx, ny))
                                q2.append((nx, ny))  # 将其添加到BFS起点队列
                    
                    # =================== 阶段2: BFS找最短路径 ===================
                    
                    # BFS逐层扩展
                    res = 0
                    while q2:
                        # 处理当前层的所有格子
                        for _ in range(len(q2)):
                            x, y = q2.popleft()
                            
                            # 检查四个相邻格子
                            for dx, dy in direct:
                                nx, ny = x + dx, y + dy
                                
                                # 检查边界
                                if 0 <= nx < N and 0 <= ny < N:
                                    # 🎯 找到第二个岛屿！
                                    if grid[nx][ny] == 1:
                                        return res
                                    
                                    # 如果是水(0)，标记并加入BFS队列
                                    if grid[nx][ny] == 0:
                                        grid[nx][ny] = 2
                                        q2.append((nx, ny))
                        
                        # 完成当前层，距离+1
                        res += 1
                    
                    return res