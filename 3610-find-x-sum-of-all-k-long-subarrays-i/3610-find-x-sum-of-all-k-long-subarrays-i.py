from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        n = len(nums)

        for i in range(n - k + 1):
            window = nums[i:i+k]
            count = Counter(window)

            top_x = sorted(count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[:x]

            total = sum(num * freq for num, freq in top_x)
            answer.append(total)

        return answer
