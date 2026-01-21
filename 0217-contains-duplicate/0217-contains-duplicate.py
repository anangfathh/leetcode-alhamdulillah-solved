class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()

        n = len(nums)

        for i in range(n):
            if nums[i] in numsSet:
                return True
            
            numsSet.add(nums[i])
        
        return False
        