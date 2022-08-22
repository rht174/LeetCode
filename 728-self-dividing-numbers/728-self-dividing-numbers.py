class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ls = []
        
        def check(num):
            num_str = str(num)
            
            if '0' in num_str:
                return False
            
            for i in num_str:
                if num % int(i) != 0:
                    return False
            return True
        
        for i in range(left, right + 1):
            if check(i) == True:
                ls.append(i)
                
        return ls