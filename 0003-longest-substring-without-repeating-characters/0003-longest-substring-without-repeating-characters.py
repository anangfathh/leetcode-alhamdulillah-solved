class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        kamus = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in kamus:
                kamus.remove(s[l])
                l += 1
            
            kamus.add(s[r])
            res = max(res, r - l + 1)
        
        return res
