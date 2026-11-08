class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            # If we matched all characters in the word
            if index == len(word):
                return True
            
            # Check boundaries and character match
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]):
                return False
            
            # Temporarily mark the cell as visited by mutating it
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions (up, down, left, right)
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )
            
            # Backtrack: restore the original character
            board[r][c] = temp
            return found

        # Start DFS from every cell that matches the first letter
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                    
        return False