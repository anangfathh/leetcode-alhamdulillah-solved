class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        def addOperation(s):
            res = ""
            for i in range(n):
                res += s[i] if i % 2 == 0 else str(((int(s[i]) + a) % 10))
            return res
        
        def rotationOperation(s):
            return s[n-b:] + s[:n-b]

        seen = set()
        def dfs(s):
            if s in seen:
                return
            seen.add(s)
            dfs(addOperation(s))
            dfs(rotationOperation(s))
            return

        dfs(s)
        return min(seen)         