class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1 }

        i = 0
        while i < len(s):
            curr = roman[s[i]]
            nextVall = roman[s[i+1]] if i+1 < len(s) else 0

            if curr >= nextVall:
                res += curr
                i += 1
            else:
                res += nextVall-curr
                i+=2
            
        return res

        