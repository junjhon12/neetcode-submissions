class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for r in range(R):
            dfs(r, 0, pac)      
            dfs(r, C - 1, atl)  
        for c in range(C):
            dfs(0, c, pac)      
            dfs(rows := R - 1, c, atl) 

        return [list(cell) for cell in pac & atl]