class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for index, row in enumerate(matrix):
            for j_index, value in enumerate(row):
                if value == target:
                    return True
        return False