class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        ends_with_one_odd = 0
        ends_with_two_odds = 0
        ends_with_one_even = 0
        ends_with_two_evens = 0
        
        for num in nums:
          if num % 2 == 1: 
            new_one_odd = (1 + ends_with_one_even + ends_with_two_evens) % MOD
            new_two_odds = ends_with_one_odd
            
            ends_with_one_odd = (ends_with_one_odd + new_one_odd) % MOD
            ends_with_two_odds = (ends_with_two_odds + new_two_odds) % MOD
            
          else: 
            new_one_even = (1 + ends_with_one_odd + ends_with_two_odds) % MOD
            
            new_two_evens = ends_with_one_even
            
            ends_with_one_even = (ends_with_one_even + new_one_even) % MOD
            ends_with_two_evens = (ends_with_two_evens + new_two_evens) % MOD

        total_stable_subsequences = (
            ends_with_one_odd + 
            ends_with_two_odds + 
            ends_with_one_even + 
            ends_with_two_evens
        ) % MOD
        
        return total_stable_subsequences