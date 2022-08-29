class Solution:
    def firstUniqChar(self, s: str) -> int:
        d1 = {}.fromkeys(s, 0)
        for i in s:
            d1[i] += 1
        
        for key , value in d1.items():
            if value == 1:
                return s.index(key)
        return -1