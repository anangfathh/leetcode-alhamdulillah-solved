class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        res = float('inf')
        s = 0

        while r < len(nums):
            s += nums[r]

            while s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
            r += 1
    
        return res if res != float('inf') else 0
                
