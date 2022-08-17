class Solution:
    def countOdds(self, low: int, high: int) -> int:
        x = (high - low) // 2
        if high % 2 != 0 or low % 2 != 0:
            x = x + 1
        return x