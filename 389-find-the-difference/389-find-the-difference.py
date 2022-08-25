class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = {}.fromkeys(s , 0)
        for i in s:
            d1[i] += 1
            
        d2 = {}.fromkeys(t , 0)
        for i in t:
            d2[i] += 1
            
        print(d1)
        print(d2)
        
        for key, value in d2.items():
            if key not in d1.keys() or value != d1[key]:
                return key
            