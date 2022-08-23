class Solution:
    def sortSentence(self, s: str) -> str:
        ls = s.split()
        new = [None] * len(ls)
        for word in ls:
        
            index = int(word[-1]) - 1
         
            new[index] = word[:-1]
            
        return " ".join(i for i in new)
