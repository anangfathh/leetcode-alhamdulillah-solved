class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        totalOnes = s.count('1')
        zerosCount = 0
        onesCount = 0
        bestScore = 0

        for i in range(n - 1):
            if s[i] == '0':
                zerosCount += 1
            else:
                onesCount += 1
        
            currentScore = zerosCount + (totalOnes - onesCount)
            bestScore = max(bestScore, currentScore)

        return bestScore



        