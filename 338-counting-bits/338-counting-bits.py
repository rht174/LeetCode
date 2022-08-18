class Solution:
    def countBits(self, n: int) -> List[int]:
        x = []
        for i in range(n+1):
            a = format(i, "b")
            summ = 0
            for j in a:
                summ += int(j)
            x.append(summ)
        return x