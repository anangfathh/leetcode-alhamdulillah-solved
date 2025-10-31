class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        res = []

        for i in count_nums.keys():
            if count_nums[i] == 2:
                res.append(i)
        
        return res

            
        