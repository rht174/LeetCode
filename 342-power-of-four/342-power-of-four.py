class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n):
            if 4 ** i == n:
                return True
            if 4 ** i > n:
                return False