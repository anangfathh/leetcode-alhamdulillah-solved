class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k <= 1:
            return True

        prev_inc = 0
        curr_inc = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_inc += 1
            else:
                if prev_inc >= k and curr_inc >= k:
                    return True
                elif curr_inc >= 2 * k:
                    return True
                prev_inc = curr_inc
                curr_inc = 1

        return (prev_inc >= k and curr_inc >= k) or curr_inc >= 2*k
