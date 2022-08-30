class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
        s = [i for i in s]
        
        idx = []
        rp = []
        
        for i, j in enumerate(s):
            if j in v:
                idx.append(i)
                rp.insert(0, j)
        
        for i, j in enumerate(idx):
            s[j] = rp[i]
        
        
        return "".join(i for i in s)