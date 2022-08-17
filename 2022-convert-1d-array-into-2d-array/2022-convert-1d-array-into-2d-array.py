class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m==1 and n ==1 and len(original) > 1:
            return []
        if n*m != len(original):
            return []
        x = []
        rp = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[rp])
                rp += 1
            x.append(row)
        return x