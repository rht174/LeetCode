class Solution:
    def hammingWeight(self, n: int) -> int:
        str_n = str(bin(n))
        return str_n.count('1')