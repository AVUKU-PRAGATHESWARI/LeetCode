class Solution(object):
    def plusOne(self, digits):
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                break
            else:
                digits[idx] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits 