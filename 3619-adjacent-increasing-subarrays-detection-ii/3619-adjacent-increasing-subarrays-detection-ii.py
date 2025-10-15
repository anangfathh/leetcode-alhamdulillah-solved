class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        curr_inc = 1
        prev_inc = 0 
        res = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr_inc += 1
            else:
                if prev_inc:
                    res = max(res, max(min(prev_inc, curr_inc), curr_inc//2))
                else:
                    res = max(res, curr_inc // 2)
                prev_inc = curr_inc
                curr_inc = 1 

        if prev_inc:
            res = max(res, max(min(prev_inc, curr_inc), curr_inc//2))
        else:
            res = max(res, curr_inc // 2)

        return res
