class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        for row, value in enumerate(mat):
            result += value[row]
        
        i = 0
        j = n-1
        while i < n or j >= 0:
            result += mat[i][j]
            i += 1
            j -= 1
            
        if n % 2 == 0:
            return result
        else:
            return result - mat[n//2][n//2]
            