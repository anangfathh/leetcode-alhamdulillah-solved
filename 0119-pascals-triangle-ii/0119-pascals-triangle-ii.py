class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_row = self.getRow(rowIndex - 1)
        current_row = [1]

        for i in range(1, rowIndex):
            current_row.append(prev_row[i - 1] + prev_row[i])
        
        current_row.append(1)

        return current_row
        