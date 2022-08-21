class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ls = []
        
        for i in nums:
            ls.append(i**2)
        
        return sorted(ls)