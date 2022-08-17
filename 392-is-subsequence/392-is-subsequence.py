class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        l = ""
        j = 0
        for i in range(len(t)):
            if j < len(s):
                if t[i] == s[j]:
                    l += t[i]
                    j += 1
        return l == s
                           