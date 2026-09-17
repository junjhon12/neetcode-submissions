class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        boxes = [set() for _ in range(len(board))]

        for row in range(len(board)):
            for column in range(len(board[0])):
                number = board[row][column]

                if number == ".":
                    continue
                
                box_index = (row // 3) * 3 + (column // 3)

                if number in rows[row] or number in cols[column] or number in boxes[box_index]:
                    return False
                
                rows[row].add(number)
                cols[column].add(number)
                boxes[box_index].add(number)
        return True