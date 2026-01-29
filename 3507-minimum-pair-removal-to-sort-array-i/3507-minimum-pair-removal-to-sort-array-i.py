class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        
        while (len(nums)) > 1:
            isAscending = True
            minSum = float("inf")
            targetIndex = -1

            for i in range(len(nums) - 1):
                pairSum = nums[i] + nums[i + 1]

                if nums[i] > nums[i + 1]:
                    isAscending = False
                
                if pairSum < minSum:
                    minSum = pairSum
                    targetIndex = i
            
            if isAscending:
                break
            
            nums[targetIndex] = minSum
            nums.pop(targetIndex + 1)
            count += 1
        
        return count


        