from typing import List
from collections import Counter

class Solution:
  def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
    n = len(nums)
    
    counts = Counter(nums)
    
    count_greater = [0] * (n + 2)
    for i in range(n, -1, -1):
        count_greater[i] = count_greater[i+1] + counts.get(i + 1, 0)

    prefix_dp = [False] * (k + 1)
    prefix_dp[0] = True
    
    answer = [False] * n
    
    for x in range(1, n + 1):
      count_of_x = counts[x]
      if count_of_x > 0:
        for _ in range(count_of_x):
          for j in range(k, x - 1, -1):
            if prefix_dp[j - x]:
              prefix_dp[j] = True
              
      found = False
      num_available_greater_than_x = count_greater[x]
      for p in range(num_available_greater_than_x + 1):
        target_sum = k - p * x
        
        if target_sum < 0:
          break
        
        if prefix_dp[target_sum]:
          found = True
          break
          
      answer[x - 1] = found
      
    return answer