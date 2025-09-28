class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return 0

        nums.sort()
        
        for i in range(n-1, 1, -1):
            a = nums[i - 2]
            b = nums [i - 1]
            c = nums[i]

            if a + b > c:
                return a + b + c
            
        return 0



        