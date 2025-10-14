class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev_inc = 0
        curr_inc = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_inc += 1
            else:
                # cek dua urutan naik yang bersebelahan
                if (prev_inc >= k and curr_inc >= k) or curr_inc >= 2 * k:
                    return True
                prev_inc = curr_inc
                curr_inc = 1

        # cek terakhir setelah loop (kalau list naik sampai akhir)
        return (prev_inc >= k and curr_inc >= k) or curr_inc >= 2 * k
