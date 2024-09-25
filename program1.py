class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
    class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(r, c):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 'L':
                    dfs(nr, nc)
        
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    dfs(r, c)
                    island_count += 1
        
        return island_count
sol = Solution()

grid1 = [
    ["L","L","L","L", "W"],
    ["L","L","W","L", "W"],
    ["L","L","W","W", "W"],
    ["W","W","W","W", "W"]
]
print(sol.getTotalIsles(grid1)) 

grid2 = [
    ["L","L","W","W", "W"],
    ["L","L","W","W", "W"],
    ["W","W","L","W", "W"],
    ["W","W","W","L", "L"]
]
print(sol.getTotalIsles(grid2))  
                    
