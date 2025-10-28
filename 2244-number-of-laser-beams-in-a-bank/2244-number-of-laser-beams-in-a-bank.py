class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ROWS,COLS = len(bank), len(bank[0])
        res = 0
        prev = 0
        for i in range(COLS):
            if bank[0][i] == '1':
                prev += 1

        for row in range (1, ROWS):
            temp = 0
            for col in range (COLS):
                if bank[row][col] == '1':
                    temp += 1
            if temp == 0:
                continue
            res += prev * temp
            prev = temp
        
        return res
