from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            r = int(math.isqrt(x))
            for i in range(3, r + 1, 2):
                if x % i == 0:
                    return False
            return True

        total = 0

        for n in nums:
            # Case 1: n = p^3
            p = round(n ** (1/3))  # perkiraan akar pangkat 3
            # koreksi sekitar p agar aman dari error float
            for cand in (p - 1, p, p + 1):
                if cand > 1 and cand ** 3 == n and is_prime(cand):
                    total += 1 + cand + cand*cand + n
                    break
            else:
                # Case 2: n = p*q (p,q prima berbeda)
                root = int(math.isqrt(n))
                found = False

                for d in range(2, root + 1):
                    if n % d == 0:
                        other = n // d
                        # Agar tepat 4 divisor, harus p dan q prima berbeda
                        if d != other and is_prime(d) and is_prime(other):
                            total += 1 + d + other + n
                        # kalau sudah ketemu satu faktor, tetap boleh break
                        # karena untuk p*q hanya ada satu faktor <= sqrt(n)
                        found = True
                        break

        return total
