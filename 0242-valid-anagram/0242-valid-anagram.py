class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}.fromkeys(s, 0)
        d2 = {}.fromkeys(t, 0)
        for i in s:
            d1[i] += 1
        for i in t:
            d2[i] += 1
            
        return d1==d2