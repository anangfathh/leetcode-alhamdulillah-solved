class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []

        for word in words:
            if len(word) != len(pattern):
                continue

            p2w = {}
            w2p = {}
            valid = True

            for p, w in zip(pattern, word):
                if p in p2w and p2w[p] != w:
                    valid = False
                    break
                if w in w2p and w2p[w] != p:
                    valid = False
                    break
                
                p2w[p] = w
                w2p[w] = p
            
            if valid == True:
                result.append(word)
        
        return result
        
        
        