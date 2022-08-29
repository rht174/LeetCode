class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d1 = dict().fromkeys(s, 0)
        for i in s:
            d1[i] += 1
            if d1[i] == 2:
                return i
        return -1
        
        