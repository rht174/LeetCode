class Solution:
    def isHappy(self, n: int) -> bool:
        def sq(x):
            x = str(x)
            sqsum = 0
            for i in x:
                sqsum += int(i)**2
            return sqsum
        
        ls =[]
        while True:
            a = sq(n)
            n = a
            if a == 1:
                return True
            if a not in ls:
                ls.append(a)
            else:
                return False