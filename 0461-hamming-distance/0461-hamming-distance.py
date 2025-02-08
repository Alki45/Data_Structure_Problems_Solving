class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_result = x ^ y
        #print(xor_result)
        return bin(xor_result).count('1')
        