class Solution:
    def addDigits(self, num: int) -> int:
        def ans(x):
            x = list(str(x))
            x = sum(map(int, x))
            
            if x < 10:
                return x
            
            return ans(x)
        
        return ans(num)