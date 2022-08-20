class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x_set = set()
        for row in matrix:
            for  j, item in enumerate(row):
                if item == 0:
                    x_set.add(j)
        
        x_list = list(x_set)
        
        if len(x_set) == 0:
            return
        
        for row in matrix:
            if 0 in row:
                for j, item in enumerate(row):
                    row[j] = 0
            k = 0
            for item in row:
                row[x_list[k]] = 0
                k += 1
                if k == len(x_list):
                    break