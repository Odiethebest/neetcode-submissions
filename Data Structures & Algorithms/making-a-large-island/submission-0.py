class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        areas = [0,0]
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 1: continue
                label = len(areas)
                stack = [(r,c)]
                grid[r][c] = label
                area = 0
                while stack:
                    x,y = stack.pop()
                    area += 1
                    for xx,yy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 1:
                            grid[xx][yy] = label
                            stack.append((xx,yy))
                areas.append(area)
        answer = max(areas)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    labels = {grid[x][y] for x,y in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)) if 0 <= x < n and 0 <= y < n}
                    answer = max(answer, 1 + sum(areas[label] for label in labels))
        return answer
