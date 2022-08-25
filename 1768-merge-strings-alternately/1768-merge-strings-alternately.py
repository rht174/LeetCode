class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ls = []
        i = 0
        j = 1
        
        w1 = w2 = 0
        
        while w1 < len(word1):
            ls.insert(i, word1[w1])
            i += 2
            w1 += 1
        
        while w2 < len(word2):
            ls.insert(j, word2[w2])
            j += 2
            w2 += 1
            
        return "".join(i for i in ls)