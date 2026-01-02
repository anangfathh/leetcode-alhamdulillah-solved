class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num_counter = Counter(nums)

        n = len(nums) // 2

        for key in num_counter.keys():
            if num_counter[key] == n:
                return key
        



        