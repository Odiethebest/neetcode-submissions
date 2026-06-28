class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        RS, CS = len(grid),len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r< 0 or c < 0 or r >= RS or c >= CS or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(RS):
            for c in range(CS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands








