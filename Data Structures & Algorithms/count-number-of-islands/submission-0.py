class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0
        # set out of grid bounds exit or is water.
        def dfs(r, c):
            if (r < 0 or c < 0 # out of bounds (left and up)
                or r >= rows or c >= cols # out of bounds (right and below)
                or grid[r][c] == "0"): # if water or sunk (traversed)
                return
        
            grid[r][c] = "0"

            dfs(r + 1, c) # check right of
            dfs(r - 1, c) # check left of
            dfs(r, c + 1) # check below of
            dfs(r, c - 1) # check above of
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c)

        return island_count