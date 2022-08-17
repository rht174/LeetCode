class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        l = 0
        j = 0
        for i in range(len(t)):
            if j < len(s):
                if t[i] == s[j]:
                    l += 1
                    j += 1
        return l == len(s)
                           