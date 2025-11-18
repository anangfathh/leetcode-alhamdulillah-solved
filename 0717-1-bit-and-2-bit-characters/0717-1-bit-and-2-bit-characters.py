class Solution:
    def isOneBitCharacter(self, bits):
        n = len(bits)
        currIndex = 0

        if bits[-1] == 1:
            return False

        while currIndex < n:
            if bits[currIndex] == 0:
                if currIndex == n - 1:
                    return True
                currIndex += 1 
            else:
                currIndex += 2 
                
        return False