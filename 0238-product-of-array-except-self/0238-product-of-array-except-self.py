class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        rightProducts = [1] * n
        leftProducts = [1] * n

        for i in range(1, n):
            leftProducts[i] = leftProducts[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            rightProducts[i] = rightProducts[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = rightProducts[i] * leftProducts[i]

        return res
        