class Solution:
    def isPalindrome(self, s: str) -> bool:
        r, l = len(s) - 1, 0

        while(l < r):
            if not (s[l].isalnum()):
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif (s[r].lower() != s[l].lower()):
                return False
            else:
                r-=1
                l+=1
        
        return True