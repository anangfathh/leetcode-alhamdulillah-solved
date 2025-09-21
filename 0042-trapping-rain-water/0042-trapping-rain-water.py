class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        lm, rm = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                l+=1
                lm = max(lm, height[l])
                res += lm - height[l]
            else:
                r-=1
                rm = max(rm, height[r])
                res += rm-height[r]
        
        return res

        