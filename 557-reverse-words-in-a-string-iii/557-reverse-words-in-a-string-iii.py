class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ls = " ".join(i[::-1] for i in s)
        return ls