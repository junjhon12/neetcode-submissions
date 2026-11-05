class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        count = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for r in range(R):
            for c in range(C):
                if grid[r][c] != '1':
                    continue

                count += 1
                grid[r][c] = '0'
                q = deque([(r, c)])

                while q:
                    cr, cc = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'    # mark BEFORE enqueue
                            q.append((nr, nc))

        return count