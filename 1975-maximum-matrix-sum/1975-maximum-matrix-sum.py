class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum_val = 0
        negativeNumber = 0
        minAbs = float('inf')
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(ROWS):
            for col in range(COLS):
                sum_val += abs(matrix[row][col])
                if matrix[row][col] < 0:
                    negativeNumber += 1
                minAbs = min(minAbs, abs(matrix[row][col]))
        
        if negativeNumber % 2 == 1:
            sum_val -= 2 * minAbs
        
        return sum_val

