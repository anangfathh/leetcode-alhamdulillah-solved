class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        mp = Counter(nums)
        min_val, max_val = min(nums), max(nums)


        pre = [0] * (max_val+1)
        for i in range(min_val, max_val+1):
            pre[i] = pre[i-1] + mp[i]
        
        def range_sum(a, b):
            a = max(a, 1)
            b = min(b, max_val)
            if a > b:
                return 0

            return pre[b] - pre[a - 1]
        
        ans = 0

        for val in range(min_val, max_val+1):
            band = range_sum(val-k, val+k)
            ans = max(ans, min(band, numOperations + mp[val]))
        
        return ans

