class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        carry = 1
        while carry and n >= 0:
            curr = digits[n] + carry
            if curr == 10:
                digits[n] = 0
                n -= 1
            else:
                digits[n] = curr
                carry = 0
            
        if carry:
            digits.insert(0, carry)
        
        return digits
