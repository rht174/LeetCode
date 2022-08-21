class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ''
        for i in digits:
            st += str(i)
        
        num = int(st) + 1
        num = str(num)
        
        return [i for i in num]