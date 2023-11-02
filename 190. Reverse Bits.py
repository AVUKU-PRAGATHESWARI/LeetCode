class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        length = len(binary)
        binary = '0'*(32-length) + binary
        binary = binary[::-1]
        n = int(binary,2)
        return n
        