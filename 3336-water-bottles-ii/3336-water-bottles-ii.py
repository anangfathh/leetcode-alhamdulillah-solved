class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            drunk += 1
            emptyBottles += 1
            numExchange += 1
        return drunk

        